"""
Chapter 07: High-Dimensional Search

Goal:
Understand why high-dimensional search is hard.

Compare:
- Brute-force nearest neighbor
- Simple KD-style recursive search
"""

# ---------- 生成数据点 ----------
import random
import time
import math

def generate_points(n, dim):
    """
    生成n个在dim维空间中的随机点
    参数:
        n: 点的数量
        dim: 维度数
    返回:
        包含n个点的列表，每个点是包含dim个坐标的列表
    """
    return [[random.random() for _ in range(dim)] for _ in range(n)]


def distance(a, b):
    """
    计算两个点之间的欧几里得距离
    参数:
        a: 第一个点（坐标列表）
        b: 第二个点（坐标列表）
    返回:
        两点之间的欧几里得距离
    """
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


# ---------- 暴力搜索方法 ----------

def brute_force(points, query):
    """
    使用暴力搜索找到查询点的最近邻
    参数:
        points: 数据点列表
        query: 查询点
    返回:
        最近邻点和它与查询点的距离
    """
    best = None  # 最佳匹配点
    best_dist = float("inf")  # 初始最大距离

    # 遍历所有点，计算距离并更新最佳匹配
    for p in points:
        d = distance(p, query)
        if d < best_dist:
            best_dist = d
            best = p

    return best, best_dist


# ---------- KD树风格的递归搜索 ----------

def kd_search(points, query, depth=0):
    """
    使用类似KD树的方法递归搜索最近邻
    参数:
        points: 当前考虑的数据点集合
        query: 查询点
        depth: 当前搜索深度（用于确定分割轴）
    返回:
        最近邻点和它与查询点的距离
    """
    # 如果没有点，则返回无穷大距离
    if not points:
        return None, float("inf")

    k = len(query)  # 获取维度数
    axis = depth % k  # 根据当前深度选择分割轴

    # 按当前轴对点进行排序
    points.sort(key=lambda x: x[axis]) # 排序
    mid = len(points) // 2  # 找到中位数位置
    median = points[mid]  # 中位数点作为当前节点

    # 根据查询点的位置决定先搜索哪个分支
    if query[axis] < median[axis]:
        next_branch = points[:mid]      # 下一搜索分支
        other_branch = points[mid+1:]   # 另一个分支（可能需要检查）
    else:
        next_branch = points[mid+1:]
        other_branch = points[:mid]

    # 在选定的分支中继续搜索
    best, best_dist = kd_search(next_branch, query, depth + 1)

    # 检查当前中位数点是否更接近
    d = distance(query, median)
    if d < best_dist:
        best, best_dist = median, d

    # 检查是否需要搜索另一个分支（剪枝优化）
    # 如果查询点到当前分割面的距离小于当前最佳距离，则需要检查另一侧
    if abs(query[axis] - median[axis]) < best_dist:
        other_best, other_dist = kd_search(other_branch, query, depth + 1)
        if other_dist < best_dist:
            best, best_dist = other_best, other_dist

    return best, best_dist


# ---------- 时间测量函数 ----------

def measure(func, *args):
    """
    测量函数执行时间
    参数:
        func: 要测量的函数
        *args: 函数参数
    返回:
        函数结果和执行时间
    """
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


# ---------- 主函数 ----------

def run():
    """运行实验比较不同维度下的搜索性能"""
    print("=== Chapter 07: High-Dimensional Search ===\n")

    # 测试不同维度下的性能
    for dim in [2, 5, 10]:
        print(f"\n--- Dimension = {dim} ---")

        # 生成测试数据点和查询点
        points = generate_points(1000, dim)
        query = [random.random() for _ in range(dim)]

        # 测量暴力搜索的时间和结果
        (_, d1), t1 = measure(brute_force, points, query)
        # 测量KD树风格搜索的时间和结果
        (_, d2), t2 = measure(kd_search, points, query)

        # 输出结果对比
        print(f"Brute Force  : dist = {d1:.6f}, time = {t1:.6f}s")
        print(f"KD-style     : dist = {d2:.6f}, time = {t2:.6f}s")


if __name__ == "__main__":
    run()