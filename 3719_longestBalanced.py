from typing import List
from collections import defaultdict


###
# 给你一个整数数组 nums。
# 如果子数组中 不同偶数 的数量等于 不同奇数 的数量，则称该 子数组 是 平衡的 。
# 返回 最长 平衡子数组的长度。
# 子数组 是数组中连续且 非空 的一段元素序列。
#
# 用dict记录奇数和偶数出现的个数，边遍历遍检查。这个方法比较慢，但是线段树的方法很复杂。
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            even = defaultdict(int)
            odd = defaultdict(int)
            for j in range(i, n):
                v = nums[j]
                if v % 2 == 0:
                    even[v] += 1
                else:
                    odd[v] += 1
                if len(even) == len(odd):
                    res = max(res, j - i + 1)
        return res