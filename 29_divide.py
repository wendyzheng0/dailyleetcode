###
# 给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
# 整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。
# 返回被除数 dividend 除以除数 divisor 得到的 商 。
# 注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−2^31,  2^31 − 1] 。本题中，如果商 严格大于 2^31 − 1 ，则返回 2^31 − 1 ；如果商 严格小于 -2^31 ，则返回 -2^31 。
#
# 严格按照环境智能存储32位有符号整数的要求有很多细节要处理。开始的时候尝试用减法不断从被除数减去除数，超时了。
# 边看题解边实现，先把dividend和divisor都统一为负数（因为负数比正数多一个），利用二分查找寻找满足y*z>=x>=y*(z+1)的z，这时候z>=0，验证等式的时候用快速乘。
# 快速乘的原理就是把z拆成2^k的和，从低到高遍历每次y翻倍，如果z的第k位为1，则把结果加上经过翻倍的y(也就是y*2^k），为了防止溢出，这里面也有很多检查。
# 二分查找的时候也有很多细节需要处理。由于0的情况被提前处理了，边界为[1，MAX]，由于边界值是可取值的，所以循环条件是left<=right。更新的时候需要另用一个变量
# 记录成功通过检查的最后结果，left和right都需要更新为非mid值。
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN, MAX = -2147483648, 2147483647
        if dividend == 0:
            return 0
        # Handle case when result may be larger than MAX
        if dividend == MIN:
            if divisor == 1:
                return MIN
            if divisor == -1:
                return MAX
        # # Handle case when result is 0
        # if divisor == MIN:
        #     return 1 if dividend == MIN else 0

        flip = False
        if dividend > 0:
            dividend = -dividend
            flip = not flip
        if divisor > 0:
            divisor = -divisor
            flip = not flip

        def quickadd(x, y, z):
            # z * y >= x > (z + 1) * y
            # x < 0, y < 0, z >= 0
            # check z * y >= x
            add = y
            result = 0
            while z > 0:
                if z & 1 == 1:
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    if add < x - add:
                        return False
                    add += add
                z = z >> 1
            return True

        left, right = 1, MAX
        res = 0
        while left <= right:
            # print(f"{left}, {right}")
            mid = left + ((right - left) >> 1)
            if quickadd(dividend, divisor, mid):
                res = mid
                if mid == MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1
        return -res if flip else res


if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(10, 3)) #3
    print(solution.divide(7, -3)) #-2
    print(solution.divide(-2147483648, -1)) #2147483647
    print(solution.divide(2147483647, 1)) #2147483647
    print(solution.divide(0, 1)) #0
    print(solution.divide(1, 1)) #1
    print(solution.divide(-2147483648, -2147483648)) #1
    print(solution.divide(-2147483647, -2147483648)) #0