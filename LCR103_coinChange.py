from typing import List
from math import inf

###
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 你可以认为每种硬币的数量是无限的。
#
# 动态规划，dp[i]表示凑成i元所需的最少硬币个数。dp[i] = min(dp[i-coins[j]] + 1), dp[0] = 0。
# 如果把coins放到外层循环可以减少里面的判断，更快一点。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
            print(dp[i])
        return dp[amount] if dp[amount] < inf else -1
