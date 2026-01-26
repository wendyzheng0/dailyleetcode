from typing import List
from math import inf


###
# 给你一个大小为 4 的整数数组 a 和一个大小 至少为 4 的整数数组 b。
# 你需要从数组 b 中选择四个下标 i0, i1, i2, 和 i3，并满足 i0 < i1 < i2 < i3。你的得分将是 a[0] * b[i0] + a[1] * b[i1] + a[2] * b[i2] + a[3] * b[i3] 的值。
# 返回你能够获得的 最大 得分。
#
# 动态规划。如果选择b[j]，则最大分数为dp[i-1][j-1] + a[i]*b[j]，其中i是a的索引，j是b的索引。
# 如果不选b[j], 则最大分数为dp[i][j-1]. pre初始化为0，因为前面没有选择任何数，cur初始化为-inf代表不可能的情况。
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n = len(b)
        # dp[i][j]: max score retrieved from a[:i+1] and b[:j+1]
        # = max(dp[i-1][j-1] + a[i]*b[j], dp[i][j-1])
        pre = [0] * (n + 1)
        cur = [-inf] * (n + 1)
        for i in range(4):
            cur[i - 2] = cur[i - 1] = -inf
            for j in range(i, n):
                cur[j] = max(pre[j - 1] + a[i] * b[j], cur[j - 1])
            pre, cur = cur, pre
            # print(pre)
        return pre[-2]
