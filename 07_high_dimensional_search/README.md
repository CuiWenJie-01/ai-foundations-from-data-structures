# Chapter 07 — High-Dimensional Search  
## Nearest Neighbor & Curse of Dimensionality

## Goal

Understand why high-dimensional search is fundamentally hard.

Even efficient structures like kd-tree begin to fail
as dimensionality increases.

---

## Data Structure Concepts

- Space partitioning
- KD-tree (conceptual)
- Nearest neighbor search
- Pruning

---

## AI Mapping

- Vector search (Embedding Retrieval)
- Similarity search
- Vector databases (FAISS, etc.)
- Curse of dimensionality

---

## Minimal AI Experiment

Experiment: KD-style search vs brute-force

- Generate random points in different dimensions
- Perform nearest neighbor search
- Compare performance as dimension increases

---

## How to Run

```bash
python experiment.py