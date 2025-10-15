from typing import List

### 3350. Maximum Number of Increasing Subarrays
# 给你一个由 n 个整数组成的数组 nums ，请你找出 k 的 最大值，使得存在 两个 相邻 且长度为 k 的 严格递增子数组。
# 具体来说，需要检查是否存在从下标 a 和 b (a < b) 开始的 两个 子数组，并满足下述全部条件：
# 这两个子数组 nums[a..a + k - 1] 和 nums[b..b + k - 1] 都是 严格递增 的。
# 这两个子数组必须是 相邻的，即 b = a + k。
# 返回 k 的 最大可能 值。
# 子数组 是数组中的一个连续 非空 的元素序列。
# 
# 题目比较直白，历遍数组记录当前递增的子数组长度。每当需要开始一个新的递增子数组时，则检查当前子数组和上一个子数组
# 可能形成的最大的k是多少。需要注意的是，两个递增子数组有可能是连续的，所以还需要检查当前子数组长度的一半。
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        part1len, curlen, maxk = 0, 1, 1
        for i in range(1, n + 1):
            if i < n and nums[i] > nums[i - 1]:
                curlen += 1
            else:
                k = min(part1len, curlen)
                maxk = max(maxk, k, curlen // 2)
                part1len = curlen
                curlen = 1
        return maxk
