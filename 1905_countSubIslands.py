from typing import List


###
# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向 （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。
# 如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。
# 请你返回 grid2 中 子岛屿 的 数目 。
#
# 用深度搜索遍历grid2里面的岛屿的每一格，遍历过程中检查grid1对应格子是不是也是岛屿，进而统计子岛屿数量。
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid1), len(grid1[0])

        def dfs(i, j):
            grid2[i][j] = 2
            res = (grid1[i][j] == 1)
            for x, y in dirs:
                ii, jj = i + x, j + y
                if 0 <= ii < m and 0 <= jj < n and grid2[ii][jj] == 1:
                    res = dfs(ii, jj) and res
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        res += 1
                    # print(f"{i},{j}: {res}")
        return res
