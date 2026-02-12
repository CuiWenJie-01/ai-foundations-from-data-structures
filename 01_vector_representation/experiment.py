import random
import math


"""
Chapter 01: Vector Representation — Embedding & Similarity

Goal:
Understand how AI systems represent the world as vectors,
and how similarity + sorting drive retrieval and reasoning.

This experiment simulates:
- Embedding vectors
- Cosine similarity
- Top-K retrieval
"""

# ---------- Vector utilities ----------
def random_vector(dim:int) -> list[float]:
    """Generate a random vector (simulated embedding)"""
    return [random.uniform(-1,1) for _ in range(dim)]

# ---------- Vector operations ----------
'''
zip 函数接收两个或多个可迭代对象（在这里是两个列表 v1 和 v2）
它会将这些可迭代对象中相同位置的元素组合成元组
例如，如果 v1 = [1, 2, 3] 和 v2 = [4, 5, 6]，那么 zip(v1,v2) 会产生 (1,4), (2,5), (3,6)
然后在列表推导式 a*b for a,b in zip(v1,v2) 中，每一对元素相乘得到 1*4, 2*5, 3*6
最后 sum 将所有乘积累加，得到点积的结果
'''
def dot(v1:list[float],v2:list[float])-> float:
    """Compute the dot product of two vectors"""
    return sum(a*b for a,b in zip(v1,v2)) # zip(v1,v2)的作用是将两个向量 v1 和 v2 中对应的元素配对起来。

# ---------- Vector similarity ----------
'''
这行代码计算向量的模长（也称为范数或大小）。

dot(v,v) 计算向量 v 与自身的点积，这意味着将向量的每个分量平方后相加：v[0]^2 + v[1]^2 + ... + v[n]^2

math.sqrt() 对上述结果取平方根

整体上，这实现了向量的 L2 范数（欧几里得范数）计算公式：||v|| = √(v[0]^2 + v[1]^2 + ... + v[n]^2)

向量的模长代表了向量在空间中的长度或大小，这是一个重要的几何概念，在计算余弦相似度等应用中非常有用。模长计算是衡量向量本身大小的基础，而不仅仅是与其他向量的关系。
'''
def norm(v:list[float])-> float:
    """Compute the norm (magnitude) of a vector"""
    return math.sqrt(dot(v,v))

def cosine_similarity(v1:list[float],v2:list[float])-> float:
    """Compute the cosine similarity between two vectors"""
    return dot(v1,v2) / (norm(v1) * norm(v2))

# ---------- Main experiment ----------
def run():
    print("=== Chapter 02: Vector Representation & Similarity ===\n")

    DIM = 8          # embedding dimension
    NUM_ITEMS = 10  # number of vectors
    TOP_K = 3

    '''
    这是Python中的字典推导式，它的作用是：
    循环遍历从 0 到 NUM_ITEMS-1 的整数（在这个例子中 NUM_ITEMS=10，所以是从 0 到 9）
    对于每个数字 i，创建一个键值对：
    键（key）：使用 f-string 格式化生成的字符串 "item_0", "item_1", ..., "item_9"
    值（value）：调用 random_vector(DIM) 函数生成一个维度为 DIM 的随机向量（在这个例子中 DIM=8）
    最终结果是创建一个包含 10 个条目的字典，每个条目都有一个唯一的标识符作为键（如 "item_0"），以及一个对应的 8 维随机向量作为值。

    这种结构模拟了实际AI系统中的嵌入向量存储方式，其中每个项目（如文档、单词或图像）都被映射到一个多维向量空间中的一个点。这样的向量可以用来表示数据的特征，并通过计算向量之间的相似性来进行检索或分类任务。

    每个向量（如 item_0、item_1 等）都是一个包含8个随机值的列表，范围在[-1, 1]之间。

    例如，item_0 可能看起来像这样：[0.34, -0.75, 0.91, -0.22, 0.56, -0.89, 0.12, 0.67]，这是一个包含8个随机浮点数的列表。 item_1 也会是一个包含8个随机浮点数的列表，以此类推。
    '''
    # Generate embeddings
    embeddings={
        f"item_{i}": random_vector(DIM)
        for i in range(NUM_ITEMS)
    }

    # Query vector
    query=random_vector(DIM) #成一个随机的查询向量，这个向量同样有8个维度，作为我们要搜索的目标。

    '''
    计算查询向量与所有已存储的嵌入向量之间的相似度：

    初始化一个空列表 similarities 来存储结果
    遍历 embeddings 字典中的每一对键值（项目名称和对应的向量）
    使用余弦相似度函数 cosine_similarity 计算查询向量与当前向量的相似度
    将项目名称和对应的相似度值作为一个元组添加到 similarities 列表中
    这个过程模拟了实际AI系统中的检索机制：给定一个查询（例如用户输入的搜索词或问题），系统会计算查询与数据库中每个项目的相似度，然后根据相似度排序，返回最匹配的结果。这是现代搜索引擎、推荐系统和RAG（检索增强生成）系统的基本原理。
    '''
    # Compute similarity
    similarities=[]
    for name,vec in embeddings.items():
        sim=cosine_similarity(query,vec)
        similarities.append((name,sim))

    '''
    1.similarities 是一个包含元组的列表，每个元组的形式为 (name, sim)，其中 name 是项目名称（如 "item_0"），sim 是该向量与查询向量的余弦相似度值。
    2.key=lambda x:x[1] 指定了排序的依据。这里的 lambda 函数 lambda x:x[1] 表示按照每个元组的第二个元素（索引为1的元素）进行排序，也就是相似度值。
    3.reverse=True 表示按降序排列，即相似度最高的项排在前面。
    
    经过这行代码处理后，similarities 列表将按照相似度从高到低排序，最相似的项目会排在列表的前面。这是检索系统的标准做法——将最相关的结果放在最前面，让用户优先看到最匹配的内容。这模拟了搜索引擎、推荐系统等的工作方式，即根据相关性对结果进行排序。
    '''
    # Sort by similarity (descending)
    similarities.sort(key=lambda x:x[1],reverse=True)

    # Output results
    print("Top-K similar items:\n")
    for name,score in similarities[:TOP_K]:
        print(f"{name:<8} similarity = {score:.4f}")

if __name__ == "__main__":
    run()