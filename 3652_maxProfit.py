from typing import List


###
# 给你两个整数数组 prices 和 strategy，其中：
# prices[i] 表示第 i 天某股票的价格。
# strategy[i] 表示第 i 天的交易策略，其中：
# -1 表示买入一单位股票。
# 0 表示持有股票。
# 1 表示卖出一单位股票。
# 同时给你一个 偶数 整数 k，你可以对 strategy 进行 最多一次 修改。一次修改包括：
# 选择 strategy 中恰好 k 个 连续 元素。
# 将前 k / 2 个元素设为 0（持有）。
# 将后 k / 2 个元素设为 1（卖出）。
# 利润 定义为所有天数中 strategy[i] * prices[i] 的 总和 。
# 返回你可以获得的 最大 可能利润。
# 注意： 没有预算或股票持有数量的限制，因此所有买入和卖出操作均可行，无需考虑过去的操作。
#
# 滑动窗口。先计算原策略，然后遍历每个可能的修改，计算修改后的利润。
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        res = sum(p * s for p, s in zip(prices, strategy))
        k2 = int(k // 2)
        newres = res
        for i in range(k2):
            newres -= prices[i] * strategy[i]
            newres += (1 - strategy[i + k2]) * prices[i + k2]
        res = max(res, newres)
        for i in range(len(prices) - k):
            newres += prices[i] * strategy[i]
            newres -= prices[i + k2]
            newres += (1 - strategy[i + k]) * prices[i + k]
            res = max(res, newres)
        return res
