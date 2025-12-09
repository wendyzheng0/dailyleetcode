from math import inf


###
# 给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。
# 注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。
#
# 从后往前遍历，找到第一个比后一个数字小的数字，把它替换为最小的比这个数字大的数字，剩下的数字从小到大排列组成新的数字。
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1
        f = 0
        right = [0] * 10
        t = n
        pre = cur = -inf
        while t > 0:
            pre = cur
            cur = t % 10
            right[cur] += 1
            t = t // 10
            f += 1
            if cur < pre:
                break
        if cur >= pre:
            return -1
        res = cur + 1
        while right[res] == 0:
            res += 1
        right[res] -= 1
        for i in range(10):
            if right[i] == 0:
                continue
            res = res * 10 ** right[i] + int('1' * right[i]) * i
        limit = (1 << 31) - 1 - t * (10 ** f)
        return -1 if res > limit else t * 10 ** f + res


if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreaterElement(12)) # 21
    print(solution.nextGreaterElement(21)) # -1
    print(solution.nextGreaterElement(124322)) # 132224
    print(solution.nextGreaterElement(2147483476)) # 2147483647
