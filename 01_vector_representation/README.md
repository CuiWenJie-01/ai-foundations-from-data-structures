# Chapter 01 — Vector Representation  
## Embedding & Similarity in AI

## Goal

Understand **how AI represents the world as numbers**,
and how similarity and sorting form the basis of retrieval,
memory, and reasoning.

---

## Data Structure Concepts

- Vector
- Inner product
- Norm
- Ordering / sorting

---

## AI Mapping

- Embedding vectors represent words, images, or concepts
- Cosine similarity measures semantic closeness
- Top-K sorting drives retrieval in:
  - Search engines
  - Recommendation systems
  - RAG pipelines

---

## Minimal AI Experiment

**Experiment: Embedding + Similarity Ranking**

- Random vectors simulate embeddings
- A query vector is compared to stored vectors
- Results are ranked by cosine similarity
- Top-K items are selected

This mirrors how real AI systems retrieve
relevant information from vector databases.

---

## How to Run

```bash
python experiment.py
