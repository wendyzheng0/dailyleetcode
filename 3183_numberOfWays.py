from functools import cache


###
# 给定 无限 数量的面值为 1，2，6 的硬币，并且 只有 2 枚硬币面值为 4。
# 给定一个整数 n ，返回用你持有的硬币达到总和 n 的方法数量。
# 因为答案可能会很大，将其 取模 109 + 7。
# 注意 硬币的顺序并不重要，[2, 2, 3] 与 [2, 3, 2] 相同。
#
# 动态规划，先用动态规划计算不限量的硬币组成 1..n面值的组合数。然后特殊处理面值4的硬币。
class Solution:
    def numberOfWays(self, n: int) -> int:
        MOD = 1_000_000_007
        coins = [1, 2, 6]
        f = [0] * (n + 1)
        f[0] = 1
        for c in coins:
            for i in range(c, n + 1):
                f[i] += f[i - c]
        res = f[n]
        if n >= 4:
            res += f[n - 4]
        if n >= 8:
            res += f[n - 8]
        return res % MOD
