from typing import List
from functools import cache


###
# 给你一个整数数组 rewardValues，长度为 n，代表奖励的值。
# 最初，你的总奖励 x 为 0，所有下标都是 未标记 的。你可以执行以下操作 任意次 ：
# 从区间 [0, n - 1] 中选择一个 未标记 的下标 i。
# 如果 rewardValues[i] 大于 你当前的总奖励 x，则将 rewardValues[i] 加到 x 上（即 x = x + rewardValues[i]），并 标记 下标 i。
# 以整数形式返回执行最优操作能够获得的 最大 总奖励。
#
# 自己用递归做的maxTotalReward1，勉强能过。看了灵神的题解，发现可以用动态规划的方法来解，并且用位运算加速。当要求的值是一个比较大的
# 范围时，可以用位运算来加速，这是一个很有用的特性，并且在python里面，不需要处理超出64位的位运算。
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        values = set()
        m = max(rewardValues)
        for reward in rewardValues:
            if reward in values:
                continue
            if reward == m - 1 or m - 1 - reward in values:
                # max possible total reward
                return m * 2 - 1
            values.add(reward)
        # assume values is sorted.
        # f[i][n] means whether can get n total rewards in values[:i], 0 <= n <= m * 2 - 1
        # f[i][n] = f[i-1][n] or f[i-1][n-values[i]](n-values[i] >= 0 and n-values[i] < values[i])
        # only consider current number
        # cur[n] = pre[n] or pre[n-curentval](currentval <= n < currentval * 2)
        # use bit to calculate to speedup
        f = 1
        for val in sorted(values):
            f |= (f & ((1 << val) - 1)) << val
        return f.bit_length() - 1

# 比最大值小的最大和-》values[:n-1]中选择元素比value[n-1]小的最大和：
# 1. values[n-2] + values[:n-2]选择比values[n-2]小的最大和
# 1.1 values[-3] + values[:-3]选择比values[-3]小的最大和
# 1.2 values[:-3]选择比values[-2]小的最大和
# 2. values[:n-2]选择元素比values[n-1]小的最大和
    def maxTotalReward1(self, rewardValues: List[int]) -> int:
        values = sorted(list(set(rewardValues)))
        if len(values) == 1:
            return values[0]

        @cache
        def dfs(n, limit):
            if limit <= 0:
                return 0
            if n == 1:
                return values[0] if values[0] < limit else 0
            res = dfs(n - 1, limit)
            if values[n - 1] < limit:
                res = max(res, values[n - 1] + dfs(n - 1,
                          min(limit - values[n - 1], values[n - 1])))
            return res
        return dfs(len(values) - 1, values[-1]) + values[-1]
