from typing import List


###
# 在两条独立的水平线上按给定的顺序写下 nums1 和 nums2 中的整数。
# 现在，可以绘制一些连接两个数字 nums1[i] 和 nums2[j] 的直线，这些直线需要同时满足：
#  nums1[i] == nums2[j]
# 且绘制的直线不与任何其他连线（非水平线）相交。
# 请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。
# 以这种方法绘制线条，并返回可以绘制的最大连线数。
#
# 动态规划：dp[i][j] 表示 nums1[:i+1] 和 nums2[:j+1] 的最大连线数。
# dp[i][j] = dp[i-1][j-1] + 1 当 nums1[i] == nums2[j]
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 当 nums1[i] != nums2[j]
# 初始化：dp[0][0] = 0
# 返回：dp[n1][n2]
# 由于dp[i][j]只与dp[i-1][j]和dp[i][j-1]有关，所以可以用两个数组优化。
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] max lines for nums1[:i+1] and nums2[:j+1]
        # = dp[i-1][j-1] + 1 when nums1[i]==nums2[j]
        # = max(dp[i-1][j], dp[i][j-1]) when nums1[i] != nums2[j]
        n1, n2 = len(nums1), len(nums2)
        pre = [0] * (n2 + 1)
        cur = [0] * (n2 + 1)
        for i in range(n1):
            for j in range(n2):
                cur[j] = max(pre[j], cur[j - 1])
                if nums1[i] == nums2[j]:
                    cur[j] = max(cur[j], pre[j - 1] + 1)
            pre, cur = cur, pre
        return pre[n2 - 1]
