from typing import List
from functools import cache
from math import inf


###
# 给你一个 n x n 的网格 grid ，代表一块樱桃地，每个格子由以下三种数字的一种来表示：
# 0 表示这个格子是空的，所以你可以穿过它。
# 1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
# -1 表示这个格子里有荆棘，挡着你的路。
# 请你统计并返回：在遵守下列规则的情况下，能摘到的最多樱桃数：
# 从位置 (0, 0) 出发，最后到达 (n - 1, n - 1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为 0 或者 1 的格子）；
# 当到达 (n - 1, n - 1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
# 当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为 0 ）；
# 如果在 (0, 0) 和 (n - 1, n - 1) 之间不存在一条可经过的路径，则无法摘到任何一个樱桃。
#
# 开始的时候是想着先用dp从（0，0）走到（n-1，n-1），然后再用dp从（n-1，n-1）走到（0，0），但是发现这样会漏掉很多情况。
# 然后看了灵神的解法发现可以用dfs来解决。由于来回的路径是起点终点交换了，所以可以看成是同样起点终点的两条路径。dfs(t, j, k)
# 表示从（0，0）出发经过t步，分别到达（t-j，j）和（t-k，k），可以收集到的最多的樱桃数量。然后利用python的cache把中间结果记下来就好了。
# 这里需要注意边界条件。如果出界了或者格子有荆棘则返回-inf，如果t==0则返回grid[0][0]和0的较大值。
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @cache
        def dfs(t, j, k):
            if not (0 <= j and 0 <= k and j <= t and k <= t and
                    grid[t - j][j] >= 0 and grid[t - k][k] >= 0):
                return -inf
            if t == 0:
                return max(grid[0][0], 0)
            res = max(dfs(t - 1, j - 1, k - 1),
                      dfs(t - 1, j - 1, k),
                      dfs(t - 1, j, k - 1),
                      dfs(t - 1, j, k))\
                + (grid[t - j][j] if grid[t - j][j] != -1 else -inf)
            if j != k:
                res += grid[t - k][k] if grid[t - k][k] != -1 else -inf
            # print(f"t:{t}, j:{j}, k:{k}, res:{res}")
            return res
        return max(dfs(2 * n - 2, n - 1, n - 1), 0)
