from math import inf


###
# 给定两个整数 n 和 m。
# 你必须从 前 m 个 质数 中选择一个多重集合，使得所选质数的和 恰好 为 n。你可以 多次 使用每个质数。
# 返回组成 n 所需的最小质数个数，如果不可能，则返回 -1。
#
# 动态规划。dp[i]表示组成i所需的最小质数个数。dp[i] = min(dp[i-p] + 1)，其中p是质数。
class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        primes = [2]
        num = 3
        while len(primes) < m and num <= n:
            for v in primes:
                if num % v == 0:
                    break
            else:
                primes.append(num)
            num += 2

        dp = [inf] * (n + 1)
        dp[0] = 0
        # print(primes)
        for p in primes:
            for v in range(p, n + 1):
                dp[v] = min(dp[v - p] + 1, dp[v])
            # print(p)
            # print(dp)
        return dp[n] if dp[n] < inf else -1
