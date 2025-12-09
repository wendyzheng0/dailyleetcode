from math import isqrt, inf


###
# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
# 动态规划。dp[i]表示凑成i的最少完全平方数个数。
class Solution:
    def numSquares(self, n: int) -> int:
        squarenum = [m * m for m in range(1, isqrt(n) + 1)]
        dp = [inf] * (n + 1)
        dp[0] = 0
        for v in squarenum:
            for i in range(v, n + 1):
                dp[i] = min(dp[i], dp[i - v] + 1)
        return dp[n]
