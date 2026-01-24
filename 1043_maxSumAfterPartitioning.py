from typing import List
from math import inf

###
# 给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。
# 返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个 32 位整数。
#
# 动态规划：dp[i] 表示 arr[:i+1] 的最大和。
# dp[i] = max(dp[i-x] + max(arr[i-x+1:i+1]) * x ) 1<=x<=k
# 初始化：dp[0] = 0
# 返回：dp[n - 1]
# 计算max(arr[i-x+1:i+1])时可以边遍历边计算。
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # dp[i] max sum can get for arr[:i]
        # = max(dp[i-x] + arr[i-x:i]) 1<=x<=k
        dp = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            mx = -inf
            for j in range(1, min(k + 1, i + 2)):
                mx = max(mx, arr[i - j + 1])
                dp[i] = max(dp[i], dp[i - j] + mx * j)
            # print(dp)
        return dp[len(arr) - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3)) # 84
    print(solution.maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4)) # 83
    print(solution.maxSumAfterPartitioning([1], 1)) # 1
    print(solution.maxSumAfterPartitioning([3,7], 2)) # 14