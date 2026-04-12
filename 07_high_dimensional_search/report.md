# Chapter 07 Report — High-Dimensional Search

## 1. 实验回顾

本章实验比较了两种最近邻搜索方法：

1. 暴力搜索（Brute Force）
2. 基于空间划分的 KD-style 搜索

在低维空间（如 2D）中：

- KD 方法可以有效剪枝
- 搜索效率较高

但随着维度上升：

> KD 方法的优势迅速减弱。

这正是本章要理解的核心问题：

> 为什么高维空间让搜索变难？

---

## 2. 关键观察（重点看趋势，而不是具体时间）

### 2.1 低维：空间是“有结构的”

在 2D 或 3D 空间中：

- 点分布相对稀疏；
- 距离差异明显；
- 空间划分有效。

这意味着：

> 可以通过“分区”快速排除大量点。

例如：

```text
一个区域明显离查询点很远 → 可以整体跳过
```
> 这正是 KD-tree 能高效的原因。

### 2.2 高维：距离开始“失去意义”

随着维度增加：

所有点之间的距离开始接近；
“最近”和“最远”差别变小；
空间变得“均匀”。

这意味着：

很难判断哪些区域可以安全剪掉。

结果是：
```
剪枝条件频繁失败；
搜索退化；
越来越接近暴力搜索。
```
### 2.3 剪枝失效：结构开始崩塌

KD-style 搜索依赖一个关键判断：

这个区域是否可能更近？

在低维：

很多区域可以直接排除；

但在高维：

几乎所有区域都“可能更近”；

于是：

剪枝几乎无法进行。

这就是所谓的：

维度灾难（Curse of Dimensionality）

---
## ai 映射
| 概念      | AI 中的真实含义    |
| ------- | ------------ |
| KD-tree | 向量空间划分       |
| 最近邻搜索   | 相似度检索        |
| 剪枝      | 减少候选         |
| 高维空间    | embedding 空间 |
| 剪枝失败    | 检索退化         |

## 为什么这对 AI 极其重要

现代 AI 几乎全部工作在高维空间：

文本 embedding（768 / 1536 维）
图像 embedding
多模态表示

如果用精确搜索：

成本极高，甚至不可行。

所以现实中采用：

ANN（近似最近邻）
向量索引
分桶 / 聚类

本质都是在解决：

高维搜索困难问题。

## 与真实 AI 系统的连接
```
这一章直接对应：

向量数据库：
FAISS
Milvus
RAG 系统：
embedding 检索
推荐系统：
相似用户 / 相似物品

这些系统都在做：

高维空间中的近邻搜索。
```

## 输出结果
```
=== Chapter 07: High-Dimensional Search ===


--- Dimension = 2 ---
Brute Force  : dist = 0.007162, time = 0.001190s
KD-style     : dist = 0.007162, time = 0.000624s

--- Dimension = 5 ---
Brute Force  : dist = 0.132054, time = 0.001685s
KD-style     : dist = 0.132054, time = 0.000533s
Brute Force  : dist = 0.007162, time = 0.001190s
KD-style     : dist = 0.007162, time = 0.000624s

--- Dimension = 5 ---
Brute Force  : dist = 0.132054, time = 0.001685s
KD-style     : dist = 0.132054, time = 0.000533s

--- Dimension = 5 ---
Brute Force  : dist = 0.132054, time = 0.001685s
KD-style     : dist = 0.132054, time = 0.000533s
Brute Force  : dist = 0.132054, time = 0.001685s
KD-style     : dist = 0.132054, time = 0.000533s
KD-style     : dist = 0.132054, time = 0.000533s

--- Dimension = 10 ---
Brute Force  : dist = 0.432280, time = 0.003053s
KD-style     : dist = 0.432280, time = 0.006451s
```