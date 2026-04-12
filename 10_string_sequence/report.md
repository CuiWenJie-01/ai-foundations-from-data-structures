# Chapter 10 Report — String / Sequence Modeling

---

## 1. 实验回顾

本章通过最简单的子串匹配问题，观察了：

> 序列数据中的重复计算问题

任务：

- 在 text 中查找 pattern
- 统计字符比较次数

---

## 2. 核心现象：重复计算

在暴力匹配中：

当某一轮匹配失败时：

- 已经比较过的字符会被丢弃
- 下一轮匹配重新开始

例如：

```text
text:    ababcabcacbab
pattern:     abcac
```

每次偏移都重新扫描 pattern。

---

## 3. 计算成本问题

最坏情况：

```text
O(n × m)
```

原因：

> 没有利用“历史匹配信息”

---

## 4. 数据结构 → AI 映射

| 概念 | AI中的含义 |
|------|------------|
| text | token sequence |
| pattern | query / sub-sequence |
| match | attention alignment |
| i-j双循环 | full pairwise attention |

---

## 5. AI 核心类比（重点）

### 5.1 字符串匹配 = attention雏形

字符串匹配在做：

> 当前模式是否与历史片段对齐

对应 Transformer：

- query vs key similarity

---

### 5.2 滑动窗口 = context window

每次 i 移动：

- 类似 attention 在 window 上滑动

---

### 5.3 重复计算 = attention 的本质问题

暴力匹配：

- 每次都重新计算所有比较

对应 AI：

- 没有 KV cache
- 没有 memory reuse

---

## 6. 本章核心认知

这一章让我理解：

> 序列模型的本质不是“单点计算”，而是“跨位置关系建模”

---

## 7. 为什么 AI 必须解决这个问题

如果不优化：

- 计算复杂度爆炸
- 长文本无法处理

因此 AI 引入：

- Attention（全局关系）
- KV Cache（避免重复计算）
- Positional Encoding（序列信息）

---

## 8. 一句话总结

> 字符串匹配 = 最原始的序列建模问题  
> AI = 在解决“如何高效建模序列关系”


## 输出结果
```
=== Chapter 10: String / Sequence Modeling ===

Text    : ababcabcacbab
Pattern : abcac

Result:
Match index: 5
Comparisons: 16
```
