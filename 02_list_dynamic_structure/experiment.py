import random

"""
Chapter 02: List & Dynamic Structures — Online Processing

Goal:
Experience the trade-off between structural flexibility
and computational efficiency in AI systems.

This experiment simulates:
- Streaming data input
- Dynamic list growth
- Online statistics update (mean, max)
"""

# ---------- Online statistics ----------

class OnlineStats:
    def __init__(self):
        self.data=[] # dynamic list
        self.count=0
        self.sum=0.0
        self.max_value=None

    def update(self,value:float):
        """Append new data and update statistics"""
        self.data.append(value)
        self.count+=1
        self.sum+=value

        if self.max_value is None or value>self.max_value:
            self.max_value=value

    """
    @property 是 Python 中的一个装饰器，它的主要作用是将一个类的方法转换为只读属性，使得我们可以像访问普通属性一样调用这个方法，而不需要使用括号。
    1.提供对内部数据的安全访问：允许外部代码访问计算得出的值，而不直接暴露内部实现
    2.保持接口一致性：即使将来改变实现方式，API 接口也不会变
    3.添加逻辑控制：在获取值时可以执行一些计算或验证逻辑
    """
    @property
    def mean(self)->float:
        """Return mean of data"""
        # 计算平均值
        return self.sum/self.count if self.count>0 else 0.0 # 防止除零错误
   
# ---------- Main experiment ----------

def run():
    print("=== Chapter 02: List & Dynamic Structures ===\n")

    stats= OnlineStats()    #创建一个 OnlineStats 对象，用于跟踪和计算统计数据。

    # Simulate streaming input
    # 生成一个包含20个随机浮点数的列表，每个数值在0到100之间，用来模拟流式数据输入。
    stream=[random.uniform(0,100) for _ in range(20)]

    """"
    遍历生成的数据流，每一步都：
    将新值添加到 stats 对象中，并更新统计信息
    打印当前步骤的详细信息
    """
    for i,value in enumerate(stream,start=1):
        stats.update(value)
        print(
            f"Step {i:02d} | " #步骤编号（两位数字，前导零补齐）
            f"new = {value:6.2f} | " #新加入的值（保留两位小数）
            f"mean = {stats.mean:6.2f} | " #当前的平均值（使用@property装饰器访问）
            f"max = {stats.max_value:6.2f}" #当前的最大值
        )

if __name__=="__main__":
    run()

"""
这个函数展示了动态数据结构的核心概念：
随着新数据的到来，系统能够实时更新统计信息（如平均值和最大值），而不需要重新处理所有历史数据。
这种"在线处理"模式在AI系统中很常见，特别是在处理流式数据时。
"""