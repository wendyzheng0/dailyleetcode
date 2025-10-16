from typing import List


####
# 给你一个下标从 0 开始、大小为 m x n 的矩阵 grid ，矩阵由若干 正 整数组成。
# 你可以从矩阵第一列中的 任一 单元格出发，按以下方式遍历 grid ：
# 从单元格 (row, col) 可以移动到 (row - 1, col + 1)、(row, col + 1) 和 (row + 1, col + 1) 三个单元格中任一满足值 严格 大于当前单元格的单元格。
# 返回你在矩阵中能够 移动 的 最大 次数。
#
# 这里使用动态规划，pre数组表示上一列能否到达，cur数组表示当前列能否到达。
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pre = [True] * m
        cur = [False] * m
        for j in range(1, n):
            for i in range(m):
                if pre[i] and grid[i][j - 1] < grid[i][j] or \
                   (i - 1 >= 0 and pre[i - 1] and grid[i - 1][j - 1] < grid[i][j]) or \
                   (i + 1 < m and pre[i + 1] and grid[i + 1][j - 1] < grid[i][j]):
                    cur[i] = True
                else:
                    cur[i] = False
            # print([grid[x][j] for x in range(m)])
            # print(f"{j}: {cur}")
            if not any(cur):
                return j - 1
            pre, cur = cur, pre
        return n - 1
