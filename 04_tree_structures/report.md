# Chapter 04 Report — Tree Structures

## 1. 实验回顾

本章通过一个简单决策树，
模拟了 AI 中最典型的一种层级结构：

> 把复杂判断拆成一连串小判断。

每次节点判断：
- 问一个问题
- 根据答案走左或右
- 最终到达叶子节点

---

## 2. 关键观察

### 2.1 树的本质不是存储，而是分裂

列表强调连续，
图强调连接，

而树强调：

> **一步步分叉决策。**

---

### 2.2 每个节点只负责一个局部问题

例如：

```text
temperature > 30?
```
---

| 树结构概念 | AI 含义  |
| ----- | ------ |
| 根节点   | 总问题入口  |
| 分支节点  | 中间推理步骤 |
| 叶子节点  | 最终答案   |
| 深度    | 推理层级   |
---
深度 = 推理层级
```
树越深：

判断越细
决策越复杂

这对应 AI 中：

更深推理链
更复杂条件组合
```

## 输出结果
```
=== Chapter 04: Tree Structures ===

Sample 1: {'temperature': 35, 'humidity': 40} -> Play No 
Sample 2: {'temperature': 25, 'humidity': 80} -> Play No 
Sample 3: {'temperature': 25, 'humidity': 50} -> Play Yes
```