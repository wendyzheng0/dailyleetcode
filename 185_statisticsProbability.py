from typing import List


###
# 你选择掷出 num 个色子，请返回所有点数总和的概率。
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 num 个骰子所能掷出的点数集合中第 i 小的那个的概率。
#
# f[i][j]表示第i个色子扔到j的概率，那么f[i][j] = 1 / 6 * f[i - 1][j - k] 第i个色子有1/6的概率扔到k（1..6)
class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        f = [0] + [1 / 6] * 6 + [0] * (num * 6 - 6)
        # f[i][j]: ith dice get value j possibility
        # f[i][j] = 1/6 * f[i-1][j-k]  1<=k<=6
        for i in range(2, num + 1):
            f2 = [0] * (6 * num + 1)
            for j in range(i, 6 * i + 1):
                for k in range(1, min(j, 6) + 1):
                    f2[j] += 1 / 6 * f[j - k]
            f = f2
        return f[num:]
