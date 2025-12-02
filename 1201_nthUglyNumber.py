import math


###
# 丑数是可以被 a 或 b 或 c 整除的 正整数 。
# 给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。
#
# 878的变形，多了一个数，所以公式变了一下。
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        right = min(a, b, c) * n
        left = min(a, b, c) + n - 2
        ab = math.lcm(a, b)
        bc = math.lcm(b, c)
        ca = math.lcm(c, a)
        abc = math.lcm(a, b, c)
        while left < right:
            mid = (left + right) // 2
            cnt = mid // a + mid // b + mid //c - mid // ab - mid // bc - mid // ca  + mid // abc
            # print(f"left:{left}, right:{right}, mid:{mid}, cnt:{cnt}")
            if cnt < n:
                left = mid + 1
            else:
                right = mid
        return right
