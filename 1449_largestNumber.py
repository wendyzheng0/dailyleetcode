from typing import List


###
# 给你一个整数数组 cost 和一个整数 target 。请你返回满足如下规则可以得到的 最大 整数：
# 给当前结果添加一个数位（i + 1）的成本为 cost[i] （cost 数组下标从 0 开始）。
# 总成本必须恰好等于 target 。
# 添加的数位中没有数字 0 。
# 由于答案可能会很大，请你以字符串形式返回。
# 如果按照上述要求无法得到任何整数，请你返回 "0" 。
#
# 用动态规划的方法逐个数位遍历，dp[i]表示总成本为i时可以得到的最大的整数。
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [None for _ in range(target + 1)]

        def larger(x, y):
            if y is None or len(x) > len(y):
                return True
            elif len(x) < len(y):
                return False
            return x > y

        dp[0] = ''
        for i in range(9):
            for j in range(cost[i], target + 1):
                if dp[j - cost[i]] is not None:
                    t = str(i + 1) + dp[j - cost[i]]
                    if larger(t, dp[j]):
                        dp[j] = t
            # print(dp)
        return dp[target] if dp[target] is not None else "0"
