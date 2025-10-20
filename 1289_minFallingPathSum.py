from bisect import bisect_left
from typing import List


###
# 给你一个 n x n 整数矩阵 grid ，请你返回 非零偏移下降路径 数字和的最小值。
# 非零偏移下降路径 定义为：从 grid 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。
#
# 只需要记住到达每行的前两小值及其列索引即可。
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mincost = []
        for i in range(n):
            v = (grid[0][i], i)
            idx = bisect_left(mincost, v)
            if idx < 2:
                mincost.insert(idx, v)
            if len(mincost) > 2:
                mincost.pop(-1)
        for i in range(1, n):
            curmincost = []
            for j in range(n):
                if mincost[0][1] == j:
                    v = (mincost[1][0] + grid[i][j], j)
                else:
                    v = (mincost[0][0] + grid[i][j], j)
                idx = bisect_left(curmincost, v)
                if idx < 2:
                    curmincost.insert(idx, v)
                if len(curmincost) > 2:
                    curmincost.pop(-1)
            mincost, curmincost = curmincost, mincost
        return mincost[0][0]
