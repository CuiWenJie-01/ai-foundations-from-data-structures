import time

"""
Chapter 01: Introduction — Complexity & Feasibility (AI Perspective)

Goal:
Build intuition for how algorithmic complexity determines
whether an AI method is computationally feasible.

This experiment compares:
- O(n)      : scalable (acceptable in AI systems)
- O(n^2)    : quickly becomes expensive (attention bottleneck)
- O(2^n)    : theoretically correct but practically infeasible
"""

# ---------- Algorithms with different complexities ----------

def linear(n: int) -> int:
    """
    O(n)
    AI meaning: scalable computation
    e.g. linear passes, streaming inference
    """
    s = 0
    for i in range(n):
        s += i
    return s


def quadratic(n: int) -> int:
    """
    O(n^2)
    AI meaning: pairwise interaction
    e.g. full attention, similarity matrices
    """
    s = 0
    for i in range(n):
        for j in range(n):
            s += i + j
    return s


def exponential(n: int) -> int:
    """
    O(2^n)
    AI meaning: unpruned search / brute-force reasoning
    Theoretically correct, but infeasible in practice.
    """
    if n <= 1:
        return 1
    return exponential(n - 1) + exponential(n - 2)


# ---------- Timing utility ----------

def measure(func, n: int):
    start = time.time()
    result = func(n)
    end = time.time()
    return end - start, result


# ---------- Main experiment ----------

def run():
    print("=== Chapter 01: Complexity & Feasibility (AI View) ===\n")

    print("[ O(n) — Scalable ]")
    for n in [10_000, 50_000, 100_000]:
        t, _ = measure(linear, n)
        print(f"n = {n:<8} time = {t:.6f}s")

    print("\n[ O(n^2) — Expensive ]")
    for n in [200, 400, 600]:
        t, _ = measure(quadratic, n)
        print(f"n = {n:<8} time = {t:.6f}s")

    print("\n[ O(2^n) — Infeasible ]")
    for n in [10, 20, 30]:
        t, _ = measure(exponential, n)
        print(f"n = {n:<8} time = {t:.6f}s")


if __name__ == "__main__":
    run()
