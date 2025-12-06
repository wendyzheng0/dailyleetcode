from typing import List
from collections import deque


###
# 给你一个整数数组 nums 和一个整数 k。你的任务是将 nums 分割成一个或多个 非空 的连续子段，使得每个子段的 最大值 与 最小值 之间的差值 不超过 k。
# 返回在此条件下将 nums 分割的总方法数。
# 由于答案可能非常大，返回结果需要对 109 + 7 取余数。
#
# 滑动窗口。维护窗口里最小值和最大值的序号，以及窗口里所有dp[i]的和。当窗口里最大值和最小值的差值超过k时，移动窗口起始位置。
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        minpos = deque()
        maxpos = deque()
        start = 0
        s = 0
        for i, v in enumerate(nums):
            s += dp[i]
            while minpos and nums[minpos[-1]] > v:
                minpos.pop()
            minpos.append(i)
            while maxpos and nums[maxpos[-1]] < v:
                maxpos.pop()
            maxpos.append(i)
            while nums[maxpos[0]] - nums[minpos[0]] > k:
                s -= dp[start]
                start += 1
                while maxpos[0] < start:
                    maxpos.popleft()
                while minpos[0] < start:
                    minpos.popleft()
            dp[i + 1] = s % MOD
        return dp[n]
