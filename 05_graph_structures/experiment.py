"""
Chapter 05: Graph Structures — Relationship Reasoning

Goal:
Understand how graphs model relationships in AI.

This experiment simulates:
- Graph relationship network
- Shortest path search between nodes
"""

# 导入双端队列，用于广度优先搜索（BFS）
from collections import deque

# ---------- 图定义 ----------
# 定义一个图，使用字典表示邻接表
# 键是节点名称，值是与该节点直接相连的邻居节点列表
graph = {
    "A": ["B", "C"],  # A节点连接到B和C节点
    "B": ["A", "D", "E"],  # B节点连接到A、D和E节点
    "C": ["A", "F"],  # C节点连接到A和F节点
    "D": ["B"],  # D节点只连接到B节点
    "E": ["B", "F"],  # E节点连接到B和F节点
    "F": ["C", "E", "G"],  # F节点连接到C、E和G节点
    "G": ["F"]  # G节点只连接到F节点
}


# ---------- 最短路径搜索（广度优先搜索BFS）----------
# 使用BFS算法查找从起始节点到目标节点的最短路径
def shortest_path(start, goal):
    """
    使用广度优先搜索算法寻找两个节点之间的最短路径
    
    参数:
    start: 起始节点
    goal: 目标节点
    
    返回:
    从起始节点到目标节点的最短路径列表，如果找不到路径则返回None
    """
    # 初始化队列，存储待探索的路径
    # 队列中的每个元素是一个路径列表，例如[['A']]代表从A开始的路径
    queue = deque([[start]])
    
    # 记录已访问过的节点，防止重复访问造成循环
    visited = set()

    # 当队列不为空时继续循环
    while queue:
        # 从队列左侧取出一个路径
        path = queue.popleft()
        # 获取当前路径的最后一个节点（即当前正在探索的节点）
        node = path[-1]

        # 如果当前节点就是目标节点，则找到了最短路径
        if node == goal:
            return path

        # 如果当前节点未被访问过
        if node not in visited:
            # 将当前节点标记为已访问
            visited.add(node)

            # 遍历当前节点的所有邻居节点
            for neighbor in graph[node]:
                # 创建新路径，将邻居节点添加到当前路径的末尾
                new_path = list(path)
                new_path.append(neighbor)
                # 将新路径添加到队列中，等待后续处理
                queue.append(new_path)

    # 如果队列为空但仍未找到目标节点，则不存在从起始点到目标点的路径
    return None


# ---------- 主函数 ----------
def run():
    """运行图结构实验的主要函数"""
    print("=== Chapter 05: Graph Structures ===\n")

    # 设置起始节点和目标节点
    start = "A"  # 起始节点
    goal = "G"   # 目标节点

    # 调用shortest_path函数计算最短路径
    path = shortest_path(start, goal)

    # 打印结果
    print(f"从 {start} 到 {goal} 的最短路径:")
    print(" -> ".join(path))


# 当此脚本作为主程序运行时执行run函数
if __name__ == "__main__":
    run()