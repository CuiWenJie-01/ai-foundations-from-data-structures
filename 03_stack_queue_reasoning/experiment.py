""""
deque（双端队列）是一个非常有用的数据结构，它允许在两端高效地添加和删除元素。
与普通的列表不同，deque在两端进行插入和删除操作的时间复杂度都是O(1)，
而普通列表在开头插入或删除元素的时间复杂度是O(n)。
"""
from collections import deque #导入deque类

"""
Chapter 03: Stack & Queue — Reasoning Process

Goal:
Understand how different data structures control
the order of processing in AI systems.

This experiment compares:
- Stack (LIFO): depth-first reasoning
- Queue (FIFO): breadth-first reasoning
"""

# ---------- Graph (state space) ----------
# 用字典表示图（Graph），有向图
graph={
    "A":["B","C"],      # 节点A连接到节点B和C
    "B":["D","E"],      # 节点B连接到节点D和E  
    "C":["F"],          # 节点C连接到节点F
    "D":[],             # 节点D没有连接到其他节点
    "E":["G"],          # 节点E连接到节点G
    "F":[],             # 节点F没有连接到其他节点
    "G":[]              # 节点G没有连接到其他节点
}
"""
    A
   / \
  B   C
 /|   |
D E   F
  |
  G
"""

# ---------- DFS using stack ----------

def dfs(start):
    print("DFS (Stack-based reasoning):")

    stack=[start] # 创建一个栈，将起始节点start加入栈中
    visited=set() # 创建一个空集合，用来记录访问过的节点

    while stack:
        node=stack.pop() # 从栈中弹出一个节点

        if node in visited: # 如果节点已经访问过，则跳过
            continue

        print(node,end=" ")
        visited.add(node) # 将节点加入访问过的节点集合

        # push neighbors (reverse to keep order intuitive)
        # 将节点的邻居加入队列，并记录访问过的节点
        for neighbor in reversed(graph[node]):
            stack.append(neighbor)

    print("\n")

# ---------- BFS using queue ----------

def bfs(start):
    print("BFS (Queue-based reasoning):")

    queue=deque([start]) # 创建一个双端队列（deque），并将起始节点start放入队列中
    visited=set([start]) # 将起始节点start加入到已访问集合中，可以确保起始节点不会被重复访问

    while queue:
        node=queue.popleft() # 从队列中取出一个节点

        print(node,end=" ")
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor) # 将未访问的邻居加入队列中，并记录访问过的节点
                visited.add(neighbor) # 将邻居加入已访问集合中

    print("\n")

# ---------- Main ----------

def run():
    print("=== Chapter 03: Stack & Queue Reasoning ===\n")
    dfs("A")
    bfs("A")

if __name__=="__main__":
    run()