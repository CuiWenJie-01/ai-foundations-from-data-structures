# Chapter 00 Report

## Observation
Even simple algorithms become unusable as complexity increases.
Exponential growth makes correctness meaningless in practice.

## AI Insight
In AI, the primary constraint is not model correctness,
but computational feasibility under realistic scale.

## Reflection
This explains why AI systems rely on approximation,
heuristics, and architectural constraints.

---
# 输出结果
=== Chapter 1: AI Feasibility & Complexity ===

[ O(n) — Linear ]
n = 10000    time = 0.000366s
n = 50000    time = 0.002262s
n = 100000   time = 0.003999s

[ O(n^2) — Quadratic ]
n = 200      time = 0.001435s
n = 400      time = 0.007190s
n = 600      time = 0.018081s

[ O(2^n) — Exponential ]
n = 10       time = 0.000013s
n = 20       time = 0.001155s
n = 30       time = 0.149258s

# 理解
✅ 实现三个函数

linear → O(n)

quadratic → O(n²)

exponential → O(2ⁿ)

✅ 输入规模逐步增大

O(n)：10k → 50k → 100k

O(n²)：200 → 400 → 600

O(2ⁿ)：10 → 20 → 30

✅ 记录运行时间

measure() 统一计时

控制变量清晰

# 对应的 AI 级直觉

O(n)
👉 可扩展推理、批处理、线性注意力
n 变大 → 时间近似线性增长
👉 AI 中“可规模化”的最低门槛

O(n²)
👉 Transformer 长上下文瓶颈（“硬墙”）
n 稍微变大 → 时间明显恶化
👉 Transformer Attention 的直觉起点

O(2ⁿ)
👉 暴力搜索、未经剪枝的推理链
👉 paper 里成立，现实中跑不动
n = 30 已经明显卡顿
👉 理论正确 ≠ AI 可用

| 代码里的概念 | AI 中对应               |
| ------ | -------------------- |
| n      | token 数 / 状态数 / 搜索深度 |
| O(n)   | 可扩展推理                |
| O(n²)  | 长上下文瓶颈               |
| O(2ⁿ)  | 搜索空间爆炸               |
| 跑不动    | 方法论上不可行              |
