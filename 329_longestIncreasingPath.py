from typing import List

###
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
#
# 记忆化搜索，记录每个点开始的最长递增路径长度。
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = [[None] * n for _ in range(m)]

        def dfs(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            longest = 1
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    longest = max(longest, dfs(ni, nj) + 1)
            memo[i][j] = longest
            return memo[i][j]

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        # print(memo)
        return res
