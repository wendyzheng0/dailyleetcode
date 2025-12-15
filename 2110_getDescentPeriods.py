from typing import List
from math import inf


###
# 给你一个整数数组 prices ，表示一支股票的历史每日股价，其中 prices[i] 是这支股票第 i 天的价格。
# 一个 平滑下降的阶段 定义为：对于 连续一天或者多天 ，每日股价都比 前一日股价恰好少 1 ，这个阶段第一天的股价没有限制。
# 请你返回 平滑下降阶段 的数目。
#
# 遍历数组，记录当前平滑下降阶段的连续天数cnt，每次遇到股价比前一日少1时，组合数都会增加cnt。
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        pre = -inf
        cnt = 1
        for p in prices:
            if p - pre == -1:
                cnt += 1
            else:
                cnt = 1
            res += cnt
            pre = p
        return res
