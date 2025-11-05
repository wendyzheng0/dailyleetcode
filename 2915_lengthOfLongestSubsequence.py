from typing import List
from math import inf


###
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 target 。
# 返回和为 target 的 nums 子序列中，子序列 长度的最大值 。如果不存在和为 target 的子序列，返回 -1 。
# 子序列 指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组。
#
# 尝试用背包问题的解法求解。f[i]表示目前遍历的数字里和为i的子序列的最大长度。由于f[i]只跟f[i]和f[i-num]有关，
# 所以可以只用一个数组来存储。
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        f = [-inf] * (target + 1)
        for num in nums:
            for i in range(target, num - 1, -1):
                f[i] = max(f[i], f[i - num] + 1)
            if num <= target:
                f[num] = max(f[num], 1)
            # print(f)
        return f[target] if f[target] > 0 else -1
