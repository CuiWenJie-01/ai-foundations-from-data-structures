import time

"""
Chapter 1 — Introduction
AI Feasibility Experiment

Goal:
Build intuition that a change in scale
fundamentally changes what is computationally possible in AI.

Experiment:
Compare runtime growth of:
- O(n)
- O(n^2)
- O(2^n)
"""

# ------------------------------
# Algorithms with different complexities
# ------------------------------
def linear(n:int)->None:
    """O(n): scalable computation"""
    s=0
    for i in range(n):
        s+=i

def quadratic(n:int)->None:
    """O(n^2): quickly becomes expensive"""
    s=0
    for i in range(n):
        for j in range(n):
            s+=i+j

def exponential(n:int)->None:
    """O(2^n): infeasible search space"""
    s=0
    if n<=1:
        return 
    exponential(n-1)
    exponential(n-2)


# ------------------------------
# Timing utility
# ------------------------------
def measure(func,n:int)->float:
    start=time.time()
    func(n)
    end=time.time()
    return end-start

# ------------------------------
# Main experiment
# ------------------------------
def run_experiment():
    print("=== Chapter 1: AI Feasibility & Complexity ===\n")

    # O(n)
    print("[ O(n) — Linear ]")
    for n in [10_000, 50_000, 100_000]:
        t = measure(linear, n)
        print(f"n = {n:<8} time = {t:.6f}s")

    # O(n^2)
    print("\n[ O(n^2) — Quadratic ]")
    for n in [200, 400, 600]:
        t = measure(quadratic, n)
        print(f"n = {n:<8} time = {t:.6f}s")

    # O(2^n)
    print("\n[ O(2^n) — Exponential ]")
    for n in [10, 20, 30]:
        t = measure(exponential, n)
        print(f"n = {n:<8} time = {t:.6f}s")


if __name__ == "__main__":
    run_experiment()