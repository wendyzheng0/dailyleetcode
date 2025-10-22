from typing import List
from math import inf


###
# 给你一个大小为 m x n 的矩阵 grid 。最初，你位于左上角 (0, 0) ，每一步，你可以在矩阵中 向右 或 向下 移动。
# 在从左上角 (0, 0) 开始到右下角 (m - 1, n - 1) 结束的所有路径中，找出具有 最大非负积 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。
# 返回 最大非负积 对 109 + 7 取余 的结果。如果最大积为 负数 ，则返回 -1 。
# 注意，取余是在得到最大积之后执行的。
# 
# 刚开始的时候记录了整数最大和负数最小精细操作，结果发现0的情况很难处理，代码写的很复杂。后来就改成
# 记录每个点上路径的最大值和最小值。然后按照从上到下从左到右的顺序历遍就好了。

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        upper = [-inf] * n
        lower = [inf] * n
        upper[0] = lower[0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                v = grid[i][j]
                if i == 0 and j == 0:
                    continue
                lo, up = inf, -inf
                if i > 0:
                    a = upper[j] * v
                    b = lower[j] * v
                    lo = min(lo, a, b)
                    up = max(up, a, b)
                if j > 0:
                    a = upper[j - 1] * v
                    b = lower[j - 1] * v
                    lo = min(lo, a, b)
                    up = max(up, a, b)
                lower[j], upper[j] = lo, up
            # print(i)
            # print(lower)
            # print(upper)
        return upper[-1] % MOD if upper[-1] >= 0 else -1
