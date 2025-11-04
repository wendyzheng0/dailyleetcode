from typing import List
from functools import cache


###
# 给定一个 下标从 0 开始 的 m x n 的 二进制 矩阵 grid ，从坐标为 (row, col) 的元素可以向右走 (row, col+1) 或向下走 (row+1, col) 。
# 返回一个布尔值，表示从 (0, 0) 出发是否存在一条路径，经过 相同 数量的 0 和 1，到达终点 (m-1, n-1) 。如果存在这样的路径返回 true ，否则返回 false 。
#
# 开始的时候用递归计算isThereAPath1，虽然也能过，但是速度很慢。于是改成递推，递推用了set来记录路径上包含的1的数量，还是很慢。
# 看了别人的题解isThereAPath，发现可以用位运算来记录路径上包含的1的数量，速度快了很多。
class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        pathlen = m + n - 1
        if pathlen & 1 != 0:
            return False
        onecnt = pathlen >> 1
        # for every grid in a line, the possible ones on the path
        dp = [0] * n
        dp[0] = 1 # at first, there is no 1 in the path
        for i in range(m):
            for j in range(n):
                if j > 0:
                    # ones from [0, 0] to [i, j] are those from [i - 1, j] and [i, j - 1]
                    dp[j] |= dp[j - 1]
                if grid[i][j]:
                    # every path adds one more
                    dp[j] = dp[j] << 1
        # check whether there are path has onecnt 1 when in [n-1, n-1]
        return dp[-1] & (1 << onecnt) != 0


    def isThereAPath1(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, target):
            if i < 0 or j < 0:
                return False
            # print(f"i:{i}, j:{j}, target:{target}")
            if grid[i][j] == 0:
                newtarget = target + 1
            else:
                newtarget = target - 1
            if i == 0 and j == 0:
                return newtarget == 0
            if dfs(i - 1, j, newtarget) \
               or dfs(i, j - 1, newtarget):
               return True
            return False

        return dfs(m - 1, n - 1, 0)