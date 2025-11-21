###
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
# 易错点，位运算的优先级比加减还要低！
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            n = -x
            mx = 1 << 31
        else:
            sign = 1
            n = x
            mx = (1 << 31) - 1
        res = 0
        while n > 0:
            if mx // 10 < res or n % 10 > (mx - res * 10):
                # print(f"mx // 10 = {mx // 10} < {res} or {n % 10} > {mx - res * 10}")
                return 0
            res = res * 10 + n % 10
            n = n // 10
        return res * sign


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(123))  # 321
    print(solution.reverse(-123)) # -321
    print(solution.reverse(120))  # 21
    print(solution.reverse(0))    # 0
    print(solution.reverse(-2147483412)) # -2143847412
    print(solution.reverse(1463847412)) # 2147483641