#!/usr/bin/env python3
"""
按周聚合各细分类别（含官媒/非官媒），计算当日热搜时长相关指标的
前后（事件日期 2024-11-12，对齐到当周周一）ITS 变化，并输出与
ITS_raw_category_official_results.xlsx 相同结构的结果表。
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import statsmodels.api as sm


PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "Data"
RAW_FILES = [
    DATA_DIR / "微博热搜202509.xlsx",
    DATA_DIR / "微博热搜数据.xlsx",
]
LABELS_PATH = DATA_DIR / "manual_host_labels.csv"
OUT_DIR = PROJECT_ROOT / "SDID_stata_6outcomes" / "v1" / "类别时间"
OUT_DIR.mkdir(parents=True, exist_ok=True)

AGG_CSV = OUT_DIR / "weekly_category_time_official.csv"
RESULT_XLSX = OUT_DIR / "ITS_category_time_official.xlsx"
RESULT_CSV = OUT_DIR / "ITS_category_time_official.csv"

EVENT_DATE = pd.Timestamp("2024-11-12")
EVENT_WEEK = EVENT_DATE - pd.to_timedelta(EVENT_DATE.weekday(), unit="D")
REQUIRED_COLS = {"时间", "当日上榜时间（分）", "主持人"}


def load_raw() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in RAW_FILES:
        if not path.exists():
            raise FileNotFoundError(f"缺少原始文件: {path}")
        frame = pd.read_excel(path)
        frame["source_file"] = path.name
        frames.append(frame)
    return pd.concat(frames, ignore_index=True)


def load_labels() -> pd.DataFrame:
    if not LABELS_PATH.exists():
        raise FileNotFoundError(f"缺少主持人标注文件: {LABELS_PATH}")
    labels = pd.read_csv(LABELS_PATH, usecols=["host", "is_official", "host_category_raw"])
    labels["host"] = labels["host"].astype(str).str.strip()
    labels["host_category_raw"] = labels["host_category_raw"].astype(str).str.strip()
    labels["is_official"] = labels["is_official"].astype(int)
    return labels.drop_duplicates(subset="host")


def normalize_raw(df: pd.DataFrame) -> pd.DataFrame:
    frame = df.rename(columns=lambda c: c.strip() if isinstance(c, str) else c).copy()
    missing = REQUIRED_COLS.difference(frame.columns)
    if missing:
        raise ValueError(f"缺少必要列: {missing}")

    frame = frame.dropna(subset=["主持人", "时间"])
    frame["主持人"] = frame["主持人"].astype(str).str.strip()
    frame["时间"] = pd.to_datetime(frame["时间"], errors="coerce")
    frame = frame.dropna(subset=["时间"])

    frame["当日上榜时间（分）"] = pd.to_numeric(frame["当日上榜时间（分）"], errors="coerce")
    frame = frame.dropna(subset=["当日上榜时间（分）"])

    # 对齐到周一的周起始日（W-SUN 周期的 start_time）
    frame["week_start"] = (
        frame["时间"] - pd.to_timedelta(frame["时间"].dt.weekday, unit="D")
    ).dt.floor("D")
    return frame


def aggregate_weekly(frame: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        frame.groupby(["week_start", "host_category_raw", "is_official"], as_index=False)
        .agg(
            weekly_total_minutes=("当日上榜时间（分）", "sum"),
            topic_count=("当日上榜时间（分）", "count"),
        )
    )

    grouped["weekly_avg_minutes"] = grouped["weekly_total_minutes"] / grouped["topic_count"].replace(0, np.nan)

    weekly_total = grouped.groupby("week_start")["weekly_total_minutes"].transform("sum")
    grouped["time_share"] = grouped["weekly_total_minutes"] / weekly_total.replace(0, np.nan)

    grouped["category"] = grouped.apply(
        lambda r: f"{r['host_category_raw']} ({'官媒' if r['is_official'] == 1 else '非官媒'})",
        axis=1,
    )

    ordered_cols = [
        "week_start",
        "category",
        "host_category_raw",
        "is_official",
        "weekly_total_minutes",
        "topic_count",
        "weekly_avg_minutes",
        "time_share",
    ]
    return grouped[ordered_cols].sort_values(["week_start", "category"])


def ma3(values: Iterable[float]) -> pd.Series:
    """三期向后滑动平均（当前及前两期）。"""
    s = pd.Series(values)
    return s.rolling(window=3, min_periods=1).mean()


def star(p: float) -> str:
    if pd.isna(p):
        return ""
    if p <= 0.01:
        return "***"
    if p <= 0.05:
        return "**"
    if p <= 0.1:
        return "*"
    return ""


def run_its(df: pd.DataFrame) -> pd.DataFrame:
    outcomes = [
        ("total_minutes", "weekly_total_minutes"),
        ("average_minutes", "weekly_avg_minutes"),
        ("time_share", "time_share"),
    ]
    records: list[dict] = []

    for category, sub in df.groupby("category"):
        sub = sub.sort_values("week_start").copy()
        sub["time_index"] = range(1, len(sub) + 1)
        sub["post"] = (sub["week_start"] >= EVENT_WEEK).astype(int)
        if sub["post"].max() == 0 or sub["post"].min() == 1:
            continue  # 无法做前后对比

        treat_idx = sub.loc[sub["post"] == 1, "time_index"].min()
        sub["time_after"] = np.where(sub["post"] == 1, sub["time_index"] - treat_idx, 0)

        for outcome, col in outcomes:
            y = sub[col]
            if y.isna().all():
                continue

            y_ma3 = ma3(y)
            X = pd.DataFrame(
                {
                    "const": 1.0,
                    "time_index": sub["time_index"],
                    "post": sub["post"],
                    "time_after": sub["time_after"],
                }
            )

            model = sm.OLS(y_ma3, X, missing="drop").fit()
            level_change = model.params.get("post", np.nan)
            slope_change = model.params.get("time_after", np.nan)
            p_level = model.pvalues.get("post", np.nan)
            p_slope = model.pvalues.get("time_after", np.nan)
            rmse = float(np.sqrt(np.mean(model.resid**2)))

            records.append(
                {
                    "outcome": outcome,
                    "category": category,
                    "Level Change": level_change,
                    "sig_level": star(p_level),
                    "p_level": p_level,
                    "Slope Change": slope_change,
                    "sig_slope": star(p_slope),
                    "p_slope": p_slope,
                    "rmse": rmse,
                    "n_obs": len(sub),
                    "start_week": sub["week_start"].min(),
                    "end_week": sub["week_start"].max(),
                }
            )

    cols = [
        "outcome",
        "category",
        "Level Change",
        "sig_level",
        "p_level",
        "Slope Change",
        "sig_slope",
        "p_slope",
        "rmse",
        "n_obs",
        "start_week",
        "end_week",
    ]
    return pd.DataFrame.from_records(records, columns=cols)


def main() -> None:
    raw = load_raw()
    labels = load_labels()
    prepared = normalize_raw(raw)
    merged = prepared.merge(labels, left_on="主持人", right_on="host", how="inner")

    weekly = aggregate_weekly(merged)
    weekly.to_csv(AGG_CSV, index=False)

    its_results = run_its(weekly)
    # 主结果（与参考表结构一致的列）
    main_cols = [
        "outcome",
        "category",
        "Level Change",
        "sig_level",
        "p_level",
        "Slope Change",
        "sig_slope",
        "p_slope",
        "rmse",
    ]
    its_results[main_cols].to_excel(RESULT_XLSX, index=False)
    its_results.to_csv(RESULT_CSV, index=False)
    print(f"周度聚合保存至: {AGG_CSV}")
    print(f"ITS 结果保存至: {RESULT_XLSX}")


if __name__ == "__main__":
    main()
