# Chapter 12 — Sorting & Ranking  
## AI 的信息组织能力

---

## 🎯 Goal

理解：

> AI 并不是“生成所有答案”，而是“排序后选择最优答案”

---

## 📌 Core Idea

排序 = 信息压缩 + 决策机制

---

## 🧪 Experiment

### Task: Similarity Ranking

步骤：

1. 生成 query 向量
2. 计算与候选向量相似度
3. 排序
4. 输出 Top-N

---

## 📊 What You Observe

### 1. 并不是所有信息都重要

AI 不会平均处理所有候选：

> 只保留 Top-K

---

### 2. 排序决定最终输出

排序结果 = 最终决策依据

---

## 🧠 AI Mapping

| 数据结构 | AI系统 |
|----------|--------|
| sort | ranking system |
| top-k | attention / beam search |
| score | similarity / probability |
| comparison | relevance judgment |

---

## 🔥 Key Insight

> AI 的“智能”不是计算，而是排序后的选择

---

## 🚀 Real AI Connection

排序机制无处不在：

### 1. Retrieval (RAG)

- 向量检索后排序
- 取 Top-K 文档

---

### 2. Transformer Attention

- attention score
- softmax 排序

---

### 3. Beam Search

- 保留 Top-N 生成路径

---

### 4. Recommendation System

- 点击率排序
- 用户兴趣排序

---

## 📌 Core Question

> 为什么 AI 总是在做“Top-K”？

→ 因为计算资源有限 + 信息过载

---

## 🧠 One-line Summary

> 排序 = AI 的注意力分配机制
