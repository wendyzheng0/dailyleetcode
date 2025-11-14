from typing import List


###
# 给你一个长度为 n 的整数数组 nums 和一个 正 整数 k 。
# 一个整数数组的 能量 定义为和 等于 k 的子序列的数目。
# 请你返回 nums 中所有子序列的 能量和 。
# 由于答案可能很大，请你将它对 109 + 7 取余 后返回。
#
# 根据提示写了个二维的动态规划，看了灵神的题解才知道还能写成一维的动态规划。本来以为用乘法算选出和为k的子序列之后剩下的元素可以组成的序列数会比较快，
# 看了一维的动态规划之后才发现直接用加法都不用算剩下元素的子序列数了。
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        dp = [0] * (k + 1)
        dp[0] = 1
        for d in nums:
            for j in range(k, -1, -1):
                dp[j] = dp[j] * 2 + (dp[j - d] if j >= d else 0)
        return dp[k] % MOD

    def sumOfPower1(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        res = 0
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # dp = [0 for _ in range(k + 1)]
        dp[0][0] = 1
        for i, d in enumerate(nums):
            for c in range(n, 0, -1):
                for j in range(k, d - 1, -1):
                    dp[c][j] = dp[c - 1][j - d] + dp[c][j]
        for c in range(n + 1):
            res += dp[c][k] * (1 << (n - c))
            res %= MOD
        return res
