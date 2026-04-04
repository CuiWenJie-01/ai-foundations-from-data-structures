# Chapter 03 — Stack & Queue  
## Reasoning Order in AI Systems

## Goal

Understand how **processing order** affects reasoning behavior in AI.

Different data structures (stack vs queue)
lead to fundamentally different exploration strategies.

---

## Data Structure Concepts

- Stack (LIFO)
- Queue (FIFO)
- Order of execution
- State exploration

---

## AI Mapping

- Stack → depth-first reasoning (DFS)
- Queue → breadth-first reasoning (BFS)
- Order determines:
  - search path
  - memory usage
  - completeness

---

## Minimal AI Experiment

**Experiment: DFS vs BFS Traversal**

- Represent a simple state space (graph)
- Use stack to simulate DFS
- Use queue to simulate BFS
- Observe different traversal orders

---

## How to Run

```bash
python experiment.py