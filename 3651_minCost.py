from typing import List
from math import inf
from heapq import heappop, heappush
from bisect import bisect_right


###
# 给你一个 m x n 的二维整数数组 grid 和一个整数 k。你从左上角的单元格 (0, 0) 出发，目标是到达右下角的单元格 (m - 1, n - 1)。
# 有两种移动方式可用：
# 普通移动：你可以从当前单元格 (i, j) 向右或向下移动，即移动到 (i, j + 1)（右）或 (i + 1, j)（下）。成本为目标单元格的值。
# 传送：你可以从任意单元格 (i, j) 传送到任意满足 grid[x][y] <= grid[i][j] 的单元格 (x, y)；此移动的成本为 0。你最多可以传送 k 次。
# 返回从 (0, 0) 到达单元格 (m - 1, n - 1) 的 最小 总成本。
#
# 开始用Dijkstra算法(minCost1)，但是由于全部可能的节点数就变成m*n*k，超时了。
# 后来用动态规划(minCost)。当k=0的人时候，就是普通的动态规划计算最短路径方法。加入了传送带之后，状态就变复杂了，但是每增加一次传送的次数，
# 对于grid[i][j]就多了一些选择，比grid[i][j]大的格子可以直接来到[i,j]，代价为0。假设上一轮到达这些格子的最小距离是minf[grid[i][j]] 因此：
# distance[i][j] = min(min(distance[i-1][j], distance[i][j-1]) + x, minf[x]), x=grid[i][j]，而每次minf也要更新。
# 灵神的题解还做了进一步的简化，distance只需要1维就可以了。
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        distance = [[inf] * (n + 1) for _ in range(m + 1)]
        mx = max(map(max, grid))
        minf = [inf] * (mx + 1)
        curminf = [inf] * (mx + 1)
        for _ in range(k + 1):
            curminf = [inf] * (mx + 1)
            for i in range(m):
                if i == 0:
                    distance[0][0] = 0
                    curminf[grid[0][0]] = 0
                else:
                    x = grid[i][0]
                    distance[i][0] = distance[i - 1][0] + x
                    distance[i][0] = min(distance[i][0], minf[x])
                    curminf[x] = min(curminf[x], distance[i][0])
                for j in range(1, n):
                    x = grid[i][j]
                    distance[i][j] = min(distance[i - 1][j], distance[i][j - 1]) + x
                    distance[i][j] = min(distance[i][j], minf[x])
                    curminf[x] = min(curminf[x], distance[i][j])
            for i in range(mx - 1, -1, -1):
                curminf[i] = min(curminf[i + 1], curminf[i])
            minf, curminf = curminf, minf
            # print("\n".join(','.join(str(v) for v in row) for row in distance))
            # print(f"minf:{minf}")
        return distance[m - 1][n - 1]

    def minCost1(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        values = [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        values.sort()
        q = [(0, 0, 0, k)]
        distance = [[[inf] * (k + 1) for _ in range(n)] for _ in range(m)]
        # print(values)
        while q:
            dist, i, j, rk = heappop(q)
            if i == m - 1 and j == n - 1:
                return dist
            if dist > distance[i][j][rk]:
                continue
            if j + 1 < n and dist + grid[i][j + 1] < distance[i][j + 1][rk]:
                distance[i][j + 1][rk] = dist + grid[i][j + 1]
                heappush(q, (dist + grid[i][j + 1], i, j + 1, rk))
            if i + 1 < m and dist + grid[i + 1][j] < distance[i + 1][j][rk]:
                distance[i + 1][j][rk] = dist + grid[i + 1][j]
                heappush(q, (dist + grid[i + 1][j], i + 1, j, rk))
            if rk > 0:
                pos = bisect_right(values, (grid[i][j], m, n))
                for idx in range(pos):
                    v, x, y = values[idx]
                    if (i != x or j != y) and dist < distance[x][y][rk - 1]:
                        distance[x][y][rk - 1] = dist
                        heappush(q, (dist, x, y, rk - 1))
            # print(q)
        return min(distance[m - 1][n - 1])
