from math import ceil


###
# 给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。
# 返回 你可以获得的最大乘积 。
#
# 当拆分成的数月平均，他们的乘积越大，所以有了integerBreak1的算法。后来发现k等于n/3的时候，乘积最大，就有了integerBreak的方法。但不知道怎么证明。
class Solution:
    def integerBreak(self, n: int) -> int:
        m = max(2, ceil(n / 3))
        x = n // m
        r = n - x * m
        return x ** (m - r) * (x + 1) ** r

    def integerBreak1(self, n: int) -> int:
        res = 0
        for k in range(2, n + 1):
            x = n // k
            r = n - x * k
            t = x ** (k - r) * (x + 1) ** r
            if t < res:
                print(k - 1)
                return res
            res = t
        return res
