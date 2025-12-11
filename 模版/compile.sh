#!/bin/bash
# LaTeX 编译脚本
# 使用 XeLaTeX 编译中文文档

cd "$(dirname "$0")"

echo "=== 第一次编译 ==="
xelatex -interaction=nonstopmode main.tex

echo "=== 编译参考文献 ==="
bibtex main

echo "=== 第二次编译 ==="
xelatex -interaction=nonstopmode main.tex

echo "=== 第三次编译 ==="
xelatex -interaction=nonstopmode main.tex

echo "=== 编译完成 ==="
echo "输出文件: main.pdf"

# 清理辅助文件（可选）
# rm -f *.aux *.bbl *.blg *.log *.out *.toc
