from typing import List
from functools import cache


###
# 给你一个 rows x cols 的矩阵 grid 来表示一块樱桃地。 grid 中每个格子的数字表示你能获得的樱桃数目。
# 你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 (0,0) 出发，机器人 2 从右上角格子 (0, cols-1) 出发。
# 请你按照如下规则，返回两个机器人能收集的最多樱桃数目：
# 从格子 (i,j) 出发，机器人可以移动到格子 (i+1, j-1)，(i+1, j) 或者 (i+1, j+1) 。
# 当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。
# 当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。
# 两个机器人在任意时刻都不能移动到 grid 外面。
# 两个机器人最后都要到达 grid 最底下一行。
#
# 乍一看想不到怎么解，看了灵神的解法发现也就增加新的状态记录下来就好了。dfs(i, j, k)表示从(i,j)和(i,k)出发，
# 可以收集到的最多的樱桃数量。然后利用python的cache把中间结果记下来就好了。
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, k):
            if i < 0 or j < 0 or k < 0 or i >= m or j >= n or k >= n:
                return 0
            res = max(dfs(i + 1, j - 1, k - 1), dfs(i + 1, j - 1, k), dfs(i + 1, j - 1, k + 1),
                      dfs(i + 1, j, k - 1), dfs(i + 1, j, k), dfs(i + 1, j, k + 1),
                      dfs(i + 1, j + 1, k - 1), dfs(i + 1, j + 1, k), dfs(i + 1, j + 1, k + 1))
            res += grid[i][j]
            if j != k:
                res += grid[i][k]
            # print(f"i:{i}, j:{j}, k:{k}, res:{res}")
            return res
        return dfs(0, 0, n - 1)
