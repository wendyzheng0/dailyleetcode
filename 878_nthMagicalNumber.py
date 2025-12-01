import math


###
# 一个正整数如果能被 a 或 b 整除，那么它是神奇的。
# 给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 10^9 + 7 取模 后的值。
#
# 这题用枚举这n个数的方式会超时，并不是大于某个数之后所有的数字就符合条件了，二分查找的方法并不是那么直接，需要思考一下。
# 当转换为小于某个数x的神奇数个数n之后，就可以二分了。因为x越大，n也会越大。
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 1_000_000_007
        left, right = min(a, b) + n - 2, min(a, b) * n
        lcm = math.lcm(a, b)
        while left < right:
            mid = (left + right) // 2
            cnt = mid // a + mid // b - mid // lcm
            # print(f"left:{left}, right:{right}, mid:{mid}, cnt:{cnt}")
            if cnt >= n:
                right = max(mid // a * a, mid // b * b)
            else:
                left = mid + 1
        return right % MOD


if __name__ == "__main__":
    solution = Solution()
    print(solution.nthMagicalNumber(1, 2, 3))  # 2
    print(solution.nthMagicalNumber(4, 2, 3))  # 6
    print(solution.nthMagicalNumber(5, 2, 4))  # 10
    print(solution.nthMagicalNumber(1000000000, 40000, 40000))  # 999720007