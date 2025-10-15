from functools import cache
from typing import List


###
# 3393. 统计异或值为给定值的路径数目
# 给你一个大小为 m x n 的二维整数数组 grid 和一个整数 k 。
# 你的任务是统计满足以下 条件 且从左上格子 (0, 0) 出发到达右下格子 (m - 1, n - 1) 的路径数目：
# 每一步你可以向右或者向下走，也就是如果格子存在的话，可以从格子 (i, j) 走到格子 (i, j + 1) 或者格子 (i + 1, j) 。
# 路径上经过的所有数字 XOR 异或值必须 等于 k 。
# 请你返回满足上述条件的路径总数。
# 由于答案可能很大，请你将答案对 109 + 7 取余 后返回。
#
# Python的好处是有@cache这个标签，可以很方便的实现记忆化搜索。
# dfs(i, j, xor)的意义是，来到（i, j）位置时，不包含（i, j）的当前路径的xor值是xor，
# 这种情况下从(i, j)走到终点的路径数目。
# 对于C++可以用一个二维数组记录中间计算结果。
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, xor):
            if i == m - 1 and j == n - 1:
                if xor ^ grid[i][j] == k:
                    return 1
                else:
                    return 0
            res = 0
            if i + 1 < m:
                res = dfs(i + 1, j, xor ^ grid[i][j]) % MOD
            if j + 1 < n:
                res = (res + dfs(i, j + 1, xor ^ grid[i][j])) % MOD
            return res

        return dfs(0, 0, 0)
