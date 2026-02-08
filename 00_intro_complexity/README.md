# Chapter 00 — Introduction  
## AI Feasibility and Computational Complexity

## Goal

Develop intuition that **a change in scale fundamentally changes what is computationally possible in AI**.

This chapter focuses on understanding why many AI ideas are
theoretically correct but practically infeasible,
and why computational complexity is a first-order constraint in AI system design.

---

## Data Structure Concepts

- Problem size and input scale
- Time complexity: O(n), O(n²), O(2ⁿ)
- Asymptotic growth
- Recursive computation

---

## AI Mapping

This chapter corresponds to core feasibility questions in AI:

- Why Transformer attention hits an **O(n²) hard wall**
- Why brute-force reasoning and unpruned search explode exponentially
- Why scalability matters more than correctness in real AI systems
- Why approximation and heuristics are unavoidable in practice

---

## Minimal AI Experiment

**Experiment: Impact of Complexity on AI Inference Time**

The experiment implements three functions with different complexities:
- Linear time: O(n)
- Quadratic time: O(n²)
- Exponential time: O(2ⁿ)

By gradually increasing input size and measuring runtime,
the experiment demonstrates how different growth rates
lead to fundamentally different feasibility outcomes.

---

## How to Run

```bash
python experiment.py
