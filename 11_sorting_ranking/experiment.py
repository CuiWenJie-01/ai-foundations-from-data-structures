import random
import math

"""
Chapter 12: Sorting & Ranking

Goal:
Understand how AI organizes information via ranking.

Experiment:
- Compute similarity between query and candidates
- Sort by score
- Extract Top-N results
"""


# ---------- 余弦相似度计算 ----------

def cosine_similarity(a, b):
    """
    计算两个向量之间的余弦相似度
    参数:
        a: 第一个向量
        b: 第二个向量
    返回:
        余弦相似度值，范围在[-1, 1]之间，值越大表示越相似
    """
    # 计算向量a和b的点积
    """
    zip(a, b) - 将两个向量的对应元素配对成元组
    (x * y for x, y in zip(a, b)) - 生成器表达式，对每一对对应元素进行乘法运算
    sum(...) - 将所有乘积求和
    """
    dot = sum(x * y for x, y in zip(a, b))
    
    # 计算向量a的模长（欧几里得范数）
    norm_a = math.sqrt(sum(x * x for x in a))
    
    # 计算向量b的模长（欧几里得范数）
    norm_b = math.sqrt(sum(x * x for x in b))
    
    # 计算余弦相似度，添加小常数防止除零错误
    return dot / (norm_a * norm_b + 1e-8)


# ---------- 生成模拟嵌入向量 ----------

def generate_vector(dim=8):
    """
    生成指定维度的随机向量
    参数:
        dim: 向量的维度，默认为8
    返回:
        包含随机浮点数的向量
    """
    return [random.random() for _ in range(dim)]


def generate_dataset(n=10, dim=8):
    """
    生成包含n个向量的数据集
    参数:
        n: 向量的数量，默认为10
        dim: 每个向量的维度，默认为8
    返回:
        包含n个随机向量的列表
    """
    return [generate_vector(dim) for _ in range(n)]


# ---------- 排名函数 ----------

def rank(query, candidates, top_k=3):
    """
    根据与查询向量的相似度对候选项进行排名
    参数:
        query: 查询向量
        candidates: 候选向量列表
        top_k: 返回的顶级结果数量，默认为3
    返回:
        包含(索引, 相似度分数)元组的列表，按分数降序排列，只返回前k个
    """
    scored = []  # 存储(索引, 相似度分数)的列表

    # 遍历所有候选向量，计算与查询向量的相似度
    for i, vec in enumerate(candidates):
        # 计算查询向量与当前候选向量的余弦相似度
        score = cosine_similarity(query, vec)
        # 将索引和分数作为一个元组添加到列表中
        scored.append((i, score))

    # 按相似度分数降序排序
    # key=lambda x: x[1] 表示按元组的第二个元素（即分数）排序
    # reverse=True 表示降序排列
    scored.sort(key=lambda x: x[1], reverse=True)

    # 返回前top_k个结果
    return scored[:top_k]


# ---------- 主函数 ----------

def run():
    """运行排序与排名实验"""
    print("=== Chapter 11: Sorting & Ranking ===\n")

    # 生成查询向量
    query = generate_vector()
    # 生成包含10个候选项的数据集
    candidates = generate_dataset(10)

    # 对候选项进行排名，返回前3个最相似的结果
    topk = rank(query, candidates, top_k=3)

    print("Top-K Results:\n")  # 输出结果标题

    # 打印排名结果
    for idx, score in topk:
        print(f"Candidate {idx} | score = {score:.4f}")  # 显示候选者索引和相似度分数（保留4位小数）


if __name__ == "__main__":
    run()