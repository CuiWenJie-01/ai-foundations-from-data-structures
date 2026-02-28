# Chapter 02 — List & Dynamic Structures  
## Dynamic Data in AI Systems

## Goal

Understand the trade-off between **structural flexibility**
and **computational efficiency** in AI systems.

Lists represent one of the most common dynamic structures
used to handle variable-length data and streaming input.

---

## Data Structure Concepts

- Dynamic array (list)
- Append operation
- Incremental update
- Variable-length sequence

---

## AI Mapping

- Lists model token sequences and context windows
- Dynamic growth mirrors streaming and online settings
- Incremental statistics reflect real-time inference

---

## Minimal AI Experiment

**Experiment: Online Data Append & Processing**

- Simulate streaming data with a list
- Append new data points dynamically
- Update statistics (mean, max) incrementally
- Avoid recomputation over the full dataset

This mirrors how AI systems process:
- Online learning
- Streaming inference
- Variable-length sequences

---

## How to Run

```bash
python experiment.py