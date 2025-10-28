from typing import List


###
# 给你一个 m x n 的整数网格图 grid ，你可以从一个格子移动到 4 个方向相邻的任意一个格子。
# 请你返回在网格图中从 任意 格子出发，达到 任意 格子，且路径中的数字是 严格递增 的路径数目。由于答案可能会很大，请将结果对 109 + 7 取余 后返回。
# 如果两条路径中访问过的格子不是完全相同的，那么它们视为两条不同的路径。
#
# 记忆化搜索，记录每个点开始的路径数。
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        memo = [[None] * n for _ in range(m)]
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            paths = 1
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    paths += dfs(ni, nj)
            memo[i][j] = paths
            return memo[i][j] % MOD

        res = 0
        for i in range(m):
            for j in range(n):
                res = (res + dfs(i, j)) % MOD
        # print(memo)
        return res
