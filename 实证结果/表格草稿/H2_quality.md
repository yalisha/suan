# 表5 情绪/信息质量的ITS与DID结果（政策日：2024-11-12）

## 5A 情绪价值 ITS（信息差/唤醒度）

来源：`manuscript/实证结果/03_H2_内容质量分化/its_all_groups_summary.csv`（社会类情绪价值）。指标含义：信息差值越高标题越夸张；斜率为政策后趋势变化。

| 组别 | 指标 | 水平效应 Post | p值 | 趋势效应 Post×Trend | p值 |
| --- | --- | --- | --- | --- | --- |
| 社会（整体） | information_gap_sum | -0.561 | 0.036 | +0.00265 | 0.092 |
| 社会（非官方） | information_gap_sum | -0.561 | 0.036 | +0.00265 | 0.092 |
| 社会（官方） | information_gap_sum | +0.007 | 0.91 | -0.00011 | 0.71 |
| 社会（整体） | arousal_sum | -0.264 | 0.244 | -0.00223 | 0.069 |
| 社会（非官方） | arousal_sum | -0.264 | 0.244 | -0.00223 | 0.069 |
| 社会（官方） | arousal_sum | +0.001 | 0.80 | +0.00014 | 0.85 |
| 娱乐核心（明星，overall） | information_gap_sum | -0.0046 | 0.676 | +0.00306 | 0.111 |
| 娱乐核心（游戏，overall） | information_gap_sum | -0.0142 | 0.571 | +0.00491 | 0.255 |
| 娱乐核心（综艺，overall） | information_gap_sum | -0.0009 | 0.848 | -0.00109 | 0.185 |
| 娱乐核心（电视剧，overall） | information_gap_sum | +0.0115 | 0.026 | +0.00152 | 0.074 |

## 5B 情绪价值 DID（官媒×Post，社会类）

来源：`manuscript/实证结果/03_H2_内容质量分化/did_regression_results_summary_bert.csv`（BERT情绪价值）。

| 指标 | 官媒×Post 系数 | p值 |
| --- | --- | --- |
| information_gap | -0.0205 | 8.7e-18 |
| arousal_index | +0.0051 | 0.0289 |

解读：DID 捕捉官媒相对非官媒的净效应，信息差显著下降、唤醒度小幅上升，表明官方信源标题规范性提升。
