import time
import random

"""
Chapter 08: Hashing & Memory Mapping

Goal:
Understand fast memory access in AI.

Compare:
- Linear search (scan)
- Hash lookup (dict)
"""

# ---------- 生成模拟嵌入表 ----------

def generate_vocab(n):
    """
    生成词汇表
    参数:
        n: 词汇表大小
    返回:
        包含n个token字符串的列表
    """
    return [f"token_{i}" for i in range(n)]


def generate_embeddings(vocab, dim=8):
    """
    为词汇表中的每个token生成对应的嵌入向量
    参数:
        vocab: 词汇表列表
        dim: 嵌入向量的维度，默认为8
    返回:
        字典，键为token，值为随机生成的嵌入向量
    """
    return {token: [random.random() for _ in range(dim)] for token in vocab}


# ---------- 线性搜索 ----------

def linear_lookup(vocab, embeddings, target):
    """
    使用线性搜索查找目标token的嵌入向量
    参数:
        vocab: 词汇表列表
        embeddings: 嵌入向量字典
        target: 目标token
    返回:
        目标token对应的嵌入向量，如果未找到则返回None
    """
    # 遍历词汇表中的每个token
    for token in vocab:
        if token == target:  # 如果找到目标token
            return embeddings[token]  # 返回对应的嵌入向量
    return None  # 未找到目标token


# ---------- 哈希查找 ----------

def hash_lookup(embeddings, target):
    """
    使用哈希查找获取目标token的嵌入向量
    Python中的字典(dict)底层使用哈希表实现，因此查找时间复杂度为O(1)
    参数:
        embeddings: 嵌入向量字典（哈希表）
        target: 目标token
    返回:
        目标token对应的嵌入向量，如果未找到则返回None
    """
    return embeddings.get(target, None)


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
    start = time.time()  # 开始计时
    result = func(*args)  # 执行函数
    end = time.time()    # 结束计时
    return result, end - start  # 返回结果和耗时


# ---------- 主函数 ----------

def run():
    """运行实验比较线性搜索和哈希查找的性能差异"""
    print("=== Chapter 08: Hashing & Memory ===\n")

    # 生成包含100,000个token的词汇表
    vocab = generate_vocab(100000)
    # 为词汇表中的每个token生成8维的嵌入向量
    embeddings = generate_embeddings(vocab)

    # 随机选择一个token作为目标查找对象
    target = random.choice(vocab)

    # 测量线性搜索的执行时间和结果
    (_, t1) = measure(linear_lookup, vocab, embeddings, target)
    # 测量哈希查找的执行时间和结果
    (_, t2) = measure(hash_lookup, embeddings, target)

    print(f"Target token: {target}\n")

    print("[ Linear Lookup - 线性查找 ]")
    print(f"time = {t1:.8f}s\n")  # 线性查找耗时，时间复杂度O(n)

    print("[ Hash Lookup - 哈希查找 ]")
    print(f"time = {t2:.8f}s")    # 哈希查找耗时，平均时间复杂度O(1)


if __name__ == "__main__":
    run()