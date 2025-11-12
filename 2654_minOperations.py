from typing import List
from math import gcd, inf


###
# 给你一个下标从 0 开始的 正 整数数组 nums 。你可以对数组执行以下操作 任意 次：
# 选择一个满足 0 <= i < n - 1 的下标 i ，将 nums[i] 或者 nums[i+1] 两者之一替换成它们的最大公约数。
# 请你返回使数组 nums 中所有元素都等于 1 的 最少 操作次数。如果无法让数组全部变成 1 ，请你返回 -1 。
# 两个正整数的最大公约数指的是能整除这两个数的最大正整数。
#
# 刚开始以为可以任意求公约数，后来发现是要求相邻两个数求公约数，简单了很多。用dp的方法记录从i到j的公约数，
# 一旦遇到公约数为1，就更新最小长度。
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x = gcd(*nums)
        if x != 1:
            return -1
        n = len(nums)
        if 1 in nums:
            return n - nums.count(1)
        f = [] #f[i]=gcd(nums[i:j])
        minlen = inf
        for i in range(n):
            f.append(nums[i])
            for j in range(i):
                f[j] = gcd(f[j], nums[i])
                if f[j] == 1:
                    minlen = min(minlen, i - j)
        return minlen + n - 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.minOperations([2,6,3,4]))  # Expected: 4
    print(solution.minOperations([2,10,6,14]))  # Expected: -1
    print(solution.minOperations([210, 1155, 770, 462, 330]))  # Expected: 8
    print(solution.minOperations([4,2,6,3]))  # Expected: 5
    print(solution.minOperations([1,1]))  # Expected: 0
    