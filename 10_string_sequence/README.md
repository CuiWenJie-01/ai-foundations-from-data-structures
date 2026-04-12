# Chapter 10 — String / Sequence Modeling  
## AI 的序列感

---

## 🎯 Goal

理解：

> 数据不是独立的，而是“按顺序依赖”的结构

---

## 📌 Core Idea

字符串 = 最简单的序列模型

AI 处理文本：

> 本质就是在处理 token sequence

---

## 🧪 Experiment

### Task: Substring Matching

- 在 text 中查找 pattern
- 统计字符比较次数
- 观察重复计算

---

## 📊 What You Observe

### 1. 重复计算

每次匹配失败：

- 都会重新从 pattern 开头开始
- 已经匹配的信息被丢弃

---

### 2. 复杂度增长

最坏情况：

```text
O(n × m)
```

---

## 🧠 AI Mapping

| 字符串模型 | AI 模型 |
|------------|--------|
| character | token |
| substring | context window |
| match | attention alignment |
| brute force scan | full attention |

---

## 🔥 Key Insight

> 序列模型的本质 = 在时间维度上做匹配

---

## 🚀 Why This Matters in AI

Transformer 做的事情：

- token → token interaction
- sequence dependency modeling

本章就是：

> Attention 的“最原始形态”

---

## 📌 Core Question

> 为什么 AI 不能“直接记住序列结构”？

→ 引出：
- attention
- positional encoding
- KV cache
