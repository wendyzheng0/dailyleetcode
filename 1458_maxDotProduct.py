from typing import List
from math import inf


###
# 给你两个数组 nums1 和 nums2 。
# 请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。
# 数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。
#
# 动态规划。dp[i][j]表示nums1[:i+1]和nums2[:j+1]的子序列的最大点积。由于数组中的值可能为负数，所以可以选择前面的数字不要。
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        #dp[i][j] max product of sub sequence nums1[:i+1] and nums2[:j+1]
        #dp[i][j] = 
        # max(dp[i-1][j-1], 0) + nums1[i] * nums2[j]
        # dp[i-1][j]
        # dp[i][j-1]
        n1, n2 = len(nums1), len(nums2)
        dp = [[-inf] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1],
                                max(dp[i - 1][j - 1], 0) + nums1[i] * nums2[j])
        return dp[n1 - 1][n2 - 1]
