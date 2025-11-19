from typing import List


###
# 给你两个下标从 0 开始的数组 present 和 future ，present[i] 和 future[i] 分别代表第 i 支股票现在和将来的价格。每支股票你最多购买 一次 ，你的预算为 budget 。
# 求最大的收益。
#
# 0-1背包问题。 f[i][j]表示前i个股票里面，还剩j预算时的最大收益。
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        #dfs(i,j)=max(dfs(i-1,j), dfs(i-1,j-present[i]))
        f = [0] * (budget + 1)
        n = len(present)
        for i in range(n):
            for j in range(budget, present[i] - 1, -1):
                f[j] = max(f[j], f[j - present[i]] + future[i] - present[i])
        return f[budget]
