import heapq  # Python内置堆模块，用于实现优先队列
import random
import time

"""
Chapter 09: Priority Queue & Top-K

Goal:
Understand how AI selects top candidates efficiently.

Compare:
- Full sorting
- Heap-based Top-K
"""

# ---------- 生成数据 ----------

def generate_scores(n):
    """
    生成n个随机分数
    参数:
        n: 分数的数量
    返回:
        包含n个随机浮点数的列表
    """
    return [random.random() for _ in range(n)]


# ---------- 全排序方法 ----------

def full_sort_topk(scores, k):
    """
    使用全排序获取Top-K项
    参数:
        scores: 待处理的分数列表
        k: 需要选择的顶级项数
    返回:
        降序排列的Top-K项
    时间复杂度: O(n log n) - 因为需要对整个数组排序
    """
    return sorted(scores, reverse=True)[:k]


# ---------- 堆式Top-K选择 ----------

def heap_topk(scores, k):
    """
    使用最小堆获取Top-K项
    参数:
        scores: 待处理的分数列表
        k: 需要选择的顶级项数
    返回:
        降序排列的Top-K项
    时间复杂度: O(n log k) - 只维护一个大小为k的堆
    """
    heap = []  # 创建一个空的最小堆（堆顶是最小元素）

    for s in scores:
        if len(heap) < k:  # 如果堆的大小还没达到k
            # 直接将当前分数加入堆中
            heapq.heappush(heap, s)
        else:  # 如果堆已满（大小为k）
            # 检查当前分数是否大于堆中的最小值（堆顶）
            if s > heap[0]:  # heap[0]是堆中的最小值
                # 移除堆中的最小值，并将当前分数加入堆
                # heapq.heapreplace会先弹出最小值，再压入新值
                heapq.heapreplace(heap, s)

    # 最后将堆中元素按降序排列并返回
    return sorted(heap, reverse=True)


# ---------- 时间测量 ----------

def measure(func, *args):
    """
    测量函数执行时间
    参数:
        func: 要测量的函数
        *args: 函数参数
    返回:
        函数执行结果和执行时间
    """
    start = time.time()  # 记录开始时间
    result = func(*args)  # 执行函数
    end = time.time()    # 记录结束时间
    return result, end - start  # 返回结果和执行时间


# ---------- 主函数 ----------

def run():
    """运行实验比较全排序和堆式Top-K选择的性能"""
    print("=== Chapter 09: Priority Queue & Top-K ===\n")

    # 生成100,000个随机分数
    scores = generate_scores(100000)
    k = 10  # 选择Top-10

    # 测量全排序方法的执行时间
    (_, t1) = measure(full_sort_topk, scores, k)
    # 测量堆式Top-K方法的执行时间
    (_, t2) = measure(heap_topk, scores, k)

    print(f"Top-{k} selection:\n")

    print("[ Full Sort - 全排序方法 ]")
    print(f"time = {t1:.6f}s\n")  # 显示全排序方法的执行时间

    print("[ Heap (Priority Queue) - 堆（优先队列）方法 ]")
    print(f"time = {t2:.6f}s")    # 显示堆式Top-K方法的执行时间


if __name__ == "__main__":
    run()