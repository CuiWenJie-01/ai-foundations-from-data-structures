import time
import random

"""
Chapter 10: String & Sequence Modeling

Goal:
Understand sequence structure in AI.

Experiment:
- Naive substring matching
- Count comparisons
- Observe redundant computation
"""


# ---------- 子串匹配算法 ----------

def substring_match(text, pattern):
    """
    朴素子串匹配算法（也称为暴力匹配算法）
    参数:
        text: 主文本字符串
        pattern: 要搜索的模式串
    返回:
        如果找到匹配，返回匹配开始位置的索引和比较次数
        如果未找到匹配，返回-1和比较次数
    时间复杂度: O(n*m)，其中n是text长度，m是pattern长度
    """
    n, m = len(text), len(pattern)  # 获取主文本和模式串的长度
    compare_count = 0  # 初始化比较次数计数器

    # 遍历主文本中可能的起始位置
    # i 的范围是 0 到 n-m，因为模式串需要完全匹配
    for i in range(n - m + 1):
        match = True  # 假设当前位置开始的匹配成功

        # 检查从位置i开始的子串是否与模式串匹配
        for j in range(m):  # 遍历模式串的每个字符
            compare_count += 1  # 每次字符比较都计入统计

            # 比较text[i+j]和pattern[j]是否相等
            if text[i + j] != pattern[j]:
                match = False  # 发现不匹配的字符
                break  # 跳出内层循环，尝试下一个起始位置

        # 如果当前起始位置的所有字符都匹配成功
        if match:
            return i, compare_count  # 返回匹配的起始位置和比较次数

    # 遍历完所有可能的起始位置仍未找到匹配
    return -1, compare_count  # 返回-1表示未找到匹配，同时返回总比较次数


# ---------- 运行实验 ----------

def run():
    """运行字符串匹配实验，展示朴素子串匹配算法的工作过程"""
    print("=== Chapter 10: String / Sequence Modeling ===\n")  # 注意：这里应该是Chapter 10而不是11

    # 定义测试用的文本和模式串
    text = "ababcabcacbab"  # 主文本字符串
    pattern = "abcac"       # 要搜索的模式串

    # 执行子串匹配算法
    index, count = substring_match(text, pattern)

    # 输出实验结果
    print("Text    :", text)        # 输出主文本
    print("Pattern :", pattern)     # 输出模式串
    print("\nResult:")              # 输出结果标题
    print("Match index:", index)    # 输出匹配的起始位置
    print("Comparisons:", count)    # 输出总的字符比较次数


if __name__ == "__main__":
    run()