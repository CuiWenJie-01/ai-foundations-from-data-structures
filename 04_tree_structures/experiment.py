"""
Chapter 04: Tree Structures — Hierarchical Decision Making

Goal:
Understand how trees represent hierarchical decisions in AI.

This experiment simulates:
- A simple decision tree
- Step-by-step classification
"""

# ---------- Tree Node ----------
# 定义树节点类，用于构建决策树
class TreeNode:
    def __init__(self, question=None, label=None):
        # question: 节点上的判断条件（问题），如果是叶子节点则为None
        self.question = question
        # label: 叶子节点的结果标签，如果不是叶子节点则为None
        self.label = label
        # left: 左子节点，通常代表"是"或"真"的分支
        self.left = None
        # right: 右子节点，通常代表"否"或"假"的分支
        self.right = None


# ---------- Build Simple Decision Tree ----------
# 构建简单的决策树函数
def build_tree():
    """
    示例决策树结构:
        Is temperature > 30?      # 根节点：判断温度是否大于30度
           /           \
        Yes             No       # 是/否分支
       /                  \
    Play No            Is humidity > 70?  # 左叶节点和右子树的内部节点
                        /             \
                     Yes               No
                    Play No         Play Yes  # 右子树的两个叶节点
    """

    # 创建根节点，包含第一个判断条件：温度是否大于30度
    root = TreeNode("temperature > 30")

    # 温度大于30度时，直接决定不玩（左子节点）
    root.left = TreeNode(label="Play No")

    # 温度不大于30度时，进入湿度判断（右子节点）
    root.right = TreeNode("humidity > 70")
    # 湿度大于70时，不玩（右子树的左叶节点）
    root.right.left = TreeNode(label="Play No")
    # 湿度不大于70时，可以玩（右子树的右叶节点）
    root.right.right = TreeNode(label="Play Yes")

    return root


# ---------- Classification ----------
# 使用决策树对样本进行分类的函数
def classify(node, sample):
    # 当前节点不是叶子节点时（即label为None时）继续遍历
    while node.label is None:
        # 获取当前节点的判断条件
        question = node.question

        # 如果判断条件是温度相关
        if question == "temperature > 30":
            # 如果样本温度大于30度，走向左子节点
            if sample["temperature"] > 30:
                node = node.left
            # 否则走向右子节点
            else:
                node = node.right

        # 如果判断条件是湿度相关
        elif question == "humidity > 70":
            # 如果样本湿度大于70%，走向左子节点
            if sample["humidity"] > 70:
                node = node.left
            # 否则走向右子节点
            else:
                node = node.right

    # 返回最终叶子节点的标签结果
    return node.label


# ---------- Main ----------
# 主运行函数
def run():
    print("=== Chapter 04: Tree Structures ===\n")

    # 构建决策树
    tree = build_tree()

    # 准备测试样本数据，包含温度和湿度信息
    samples = [
        {"temperature": 35, "humidity": 40},  # 样本1：高温低湿
        {"temperature": 25, "humidity": 80},  # 样本2：低温高湿
        {"temperature": 25, "humidity": 50},  # 样本3：低温低湿
    ]

    # 遍历每个样本并输出分类结果
    for i, sample in enumerate(samples, start=1):
        result = classify(tree, sample)
        print(f"Sample {i}: {sample} -> {result}")


if __name__ == "__main__":
    run()