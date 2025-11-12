from typing import List
from itertools import accumulate
from functools import cache
from math import inf


###
# 有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
# 每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。
#
# 
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        presum = list(accumulate(stones))
        target = sum(stones) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for i, w in enumerate(stones):
            for j in range(min(presum[i], target), w - 1, -1):
                dp[j] = dp[j] or dp[j - w]
        for j in range(target, -1, -1):
            if dp[j]:
                return presum[-1] - 2 * j

    def lastStoneWeightII2(self, stones: List[int]) -> int:
        totalweight = sum(stones)
        finaltarget = totalweight // 2
        n = len(stones)
        postsum = stones.copy()
        for i in range(n - 1, 0, -1):
            postsum[i - 1] += postsum[i]
        print(postsum)

        @cache
        def dfs(idx, target):
            if idx >= n or target == 0:
                return target
            r1 = r2 = inf
            if postsum[idx] > target:
                r1 = dfs(idx + 1, target)
            if target >= stones[idx]:
                r2 = dfs(idx + 1, target - stones[idx])
            # print(f"{idx}, target:{target}, ret:{min(r1, r2, target)}")
            return min(r1, r2, target)

        diff = dfs(0, finaltarget)
        return totalweight - (finaltarget - diff) * 2


