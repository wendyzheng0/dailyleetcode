from typing import List
from math import inf


###
# 给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。
# 从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之 和 与目标值 target 的 绝对差 。
# 返回 最小的绝对差 。
# a 和 b 两数字的 绝对差 是 a - b 的绝对值。
#
# 由于每行都会选一个数，遍历每一行，记录到当前行所有可能的和。最后检查距离target最近的和。
# 利用位运算优化记录可能的和的过程。
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m, n = len(mat), len(mat[0])
        possiblesum = 1
        for i in range(m):
            curpossible = 0
            for j in range(n):
                curpossible |= (possiblesum << mat[i][j])
            possiblesum = curpossible
        # low = possiblesum >> target
        # high = possiblesum & ((1 << (target + 1)) - 1)
        diff = inf
        for t in range(target, -1, -1):
            if possiblesum & (1 << t):
                diff = min(target - t, diff)
                break
        t = target + 1
        while t < target + diff:
            if possiblesum & (1 << t):
                diff = min(t - target, diff)
                break
            t += 1
        return diff
