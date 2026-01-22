from typing import List
from collections import defaultdict

###
# 给定 m x n 矩阵 matrix 。
# 你可以从中选出任意数量的列并翻转其上的 每个 单元格。（即翻转后，单元格的值从 0 变成 1，或者从 1 变为 0 。）
# 返回 经过一些翻转后，行内所有值都相等的最大行数 。
#
# 开始的时候尝试循环每行构造一个int来检查有没有一样的或者取反一样的，虽然能过，但比较慢。
# 后来发现把列表转tuple会更快。
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for row in matrix:
            t = tuple(row if row[0] == 0 else [1 - v for v in row])
            cnt[t] += 1
        return max(cnt.values())
