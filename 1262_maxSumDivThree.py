from typing import List
from math import inf


###
# 给你一个整数数组 nums，请你找出并返回能被三整除的元素 最大和。
#
# 动态规划，dp[i][j]表示前i个数中，余数为j的最大的和。
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[i][j] max sum of numbers in nums[0,i], remainder is j (0, 1, 2)
        # r=nums[i] % 3, dp[i][(j+r)%3] = max(dp[i-1][j] + nums[i], dp[i-1][(j+r)%3]
        dp = [-inf] * 3
        for num in nums:
            pre = dp.copy()
            for j in range(3):
                dp[(num + j) % 3] = max(pre[j] + num, pre[(num + j) % 3])
            dp[num % 3] = max(dp[num % 3], num)
            # print(dp)
        return max(dp[0], 0)
