"""
Chapter 06: Search Trees & Pruning

Goal:
Understand how structure reduces search cost.

This experiment compares:
- Linear Scan (brute-force search)
- Binary Search Tree style search
"""

import time
import random

# ---------- Build Sorted Data ----------
# 创建一个包含10000个不重复随机数的有序数组，数值范围在1到100000之间
# 随机选择一个目标值作为搜索目标
data = sorted(random.sample(range(1, 100000), 10000))
target = random.choice(data) # 选择一个目标值


# ---------- Linear Search ----------
# 线性搜索函数：遍历整个数组直到找到目标值或到达数组末尾
# 时间复杂度 O(n)，空间复杂度 O(1)
def linear_search(arr, target):
    """
    线性搜索算法
    :param arr: 搜索的数组
    :param target: 要查找的目标值
    :return: 如果找到返回索引位置，否则返回-1
    """
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


# ---------- Binary Search (BST Idea) ----------
# 二分搜索函数：利用数组已排序的特性，每次比较后可以排除一半的数据
# 时间复杂度 O(log n)，空间复杂度 O(1)
def binary_search(arr, target):
    """
    二分搜索算法（模拟二叉搜索树的搜索方式）
    :param arr: 已排序的数组
    :param target: 要查找的目标值
    :return: 如果找到返回索引位置，否则返回-1
    """
    left = 0  # 左边界
    right = len(arr) - 1  # 右边界

    # 当左边界不超过右边界时继续搜索
    while left <= right:
        mid = (left + right) // 2  # 计算中间位置

        if arr[mid] == target:
            # 找到目标值，返回索引
            return mid
        elif arr[mid] < target:
            # 目标值在右半部分，更新左边界
            left = mid + 1
        else:
            # 目标值在左半部分，更新右边界
            right = mid - 1

    # 未找到目标值，返回-1
    return -1


# ---------- Timing Utility ----------
# 测量函数执行时间的工具函数
def measure(func, arr, target):
    """
    测量函数执行时间和结果
    :param func: 要测量的函数
    :param arr: 函数的第一个参数
    :param target: 函数的第二个参数
    :return: (执行时间, 函数返回值)
    """
    start = time.time()  # 记录开始时间
    result = func(arr, target)  # 执行函数
    end = time.time()  # 记录结束时间
    return end - start, result  # 返回执行时间及结果


# ---------- Main ----------
def run():
    """运行实验并输出结果"""
    print("=== Chapter 06: Search Trees & Pruning ===\n")
    print(f"Target = {target}\n")

    # 测试线性搜索性能
    t1, idx1 = measure(linear_search, data, target)
    print("[ Linear Search ]")
    print(f"Index: {idx1}, Time: {t1:.8f}s\n")

    # 测试二分搜索性能
    t2, idx2 = measure(binary_search, data, target)
    print("[ Binary Search ]")
    print(f"Index: {idx2}, Time: {t2:.8f}s")


if __name__ == "__main__":
    run()