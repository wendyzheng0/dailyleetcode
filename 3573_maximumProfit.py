from typing import List
from functools import cache
from math import inf


###
# 给你一个整数数组 prices，其中 prices[i] 是第 i 天股票的价格（美元），以及一个整数 k。
# 你最多可以进行 k 笔交易，每笔交易可以是以下任一类型：
# 普通交易：在第 i 天买入，然后在之后的第 j 天卖出，其中 i < j。你的利润是 prices[j] - prices[i]。
# 做空交易：在第 i 天卖出，然后在之后的第 j 天买回，其中 i < j。你的利润是 prices[i] - prices[j]。
# 注意：你必须在开始下一笔交易之前完成当前交易。此外，你不能在已经进行买入或卖出操作的同一天再次进行买入或卖出操作。
# 通过进行 最多 k 笔交易，返回你可以获得的最大总利润。
#
# 有两种操作，0表示不操作，1表示普通交易，2做空交易。dfs(i, j, state)表示第i天，最多进行j次交易，当前状态为state时的最大利润。
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        @cache
        def dfs(i, j, state):
            if j < 0:
                return -inf
            if i < 0:
                return -inf if state else 0
            if state == 0:
                return max(dfs(i - 1, j, 0), dfs(i - 1, j, 1) + prices[i], dfs(i - 1, j, 2) - prices[i])
            if state == 1:
                return max(dfs(i - 1, j, 1), dfs(i - 1, j - 1, 0) - prices[i])
            if state == 2:
                return max(dfs(i - 1, j, 2), dfs(i - 1, j - 1, 0) + prices[i])
        res = dfs(len(prices) - 1, k, 0)
        dfs.cache_clear()
        return res
