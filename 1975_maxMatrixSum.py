from typing import List
from math import inf


###
# 给你一个 n x n 的整数方阵 matrix 。你可以执行以下操作 任意次 ：
# 选择 matrix 中 相邻 两个元素，并将它们都 乘以 -1 。
# 如果两个元素有 公共边 ，那么它们就是 相邻 的。
# 你的目的是 最大化 方阵元素的和。请你在执行以上操作之后，返回方阵的 最大 和。
#
# 任意两个负数可以通过变换都变为正数，所以只需要统计负数的个数，如果为奇数，则需要减去最小的负数。
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg = sum(sum(1 for item in row if item < 0) for row in matrix)
        s = sum(sum(abs(v) for v in row) for row in matrix)
        if neg % 2 == 1:
            x = min(min(abs(v) for v in row) for row in matrix)
            s -= x * 2
        return s

    def maxMatrixSum1(self, matrix: List[List[int]]) -> int:
        neg = 0
        s = 0
        x = inf
        for row in matrix:
            for item in row:
                if item < 0:
                    neg += 1
                    item = -item
                s += item
                x = min(x, item)
        if neg % 2 == 1:
            s -= x * 2
        return s
