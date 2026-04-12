# Chapter 12 Report — Sorting & Ranking

---

## 1. 实验回顾

本章实验模拟了：

> AI 如何对多个候选信息进行排序选择

步骤：

- 计算 query 与候选向量相似度
- 根据 score 排序
- 选出 Top-K

---

## 2. 核心现象

### 2.1 信息量爆炸

候选很多，但：

> 只有少数是“真正相关”的

---

### 2.2 排序决定输出

排序结果直接影响最终选择：

- Top-1 → 最优答案
- Top-K → 多样性保留

---

## 3. 数据结构 → AI 映射

| 概念 | AI对应 |
|------|--------|
| sorting | ranking mechanism |
| score | similarity / probability |
| Top-K | attention selection |
| comparison | relevance evaluation |

---

## 4. AI 核心类比

### 4.1 排序 = 注意力分配

AI 不会平等看待所有信息：

> 而是根据 relevance 排序

---

### 4.2 Top-K = 信息压缩机制

Transformer 中：

- attention weight 排序
- 保留重要 token

---

### 4.3 排序 = 决策过程

最终输出不是“计算结果”，而是：

> 排序后的选择结果

---

## 5. 本章核心认知

这一章让我理解：

> AI 的核心能力不是“算”，而是“选”

---

## 6. 为什么排序如此重要

没有排序：

- 所有信息同等处理 → 计算爆炸

有排序：

- 只关注 Top-K → 信息压缩

---

## 7. 与真实 AI 系统的连接

### 7.1 RAG

- vector DB 检索
- rerank

---

### 7.2 Transformer

- attention score
- softmax selection

---

### 7.3 Search Engine

- PageRank
- relevance ranking

---

## 8. 一句话总结

> AI 的智能，本质是排序后的选择能力

## 输出结果
```
=== Chapter 12: Sorting & Ranking ===

Top-K Results:

Candidate 7 | score = 0.8994
Candidate 9 | score = 0.8384
Candidate 0 | score = 0.8267
```