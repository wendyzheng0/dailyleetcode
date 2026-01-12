from typing import List
from heapq import heappush, heappop
from math import inf


###
# 迷宫中有一个球，它有空地 (表示为 0) 和墙 (表示为 1)。球可以向上、向下、向左或向右滚过空地，但直到撞上墙之前它都不会停止滚动。当球停止时，它才可以选择下一个滚动方向。
# 给定 m × n 的迷宫(maze)，球的起始位置 (start = [startrow, startcol]) 和目的地 (destination = [destinationrow, destinationcol])，返回球在目的地 (destination) 停止的最短距离。如果球不能在目的地 (destination) 停止，返回 -1。
# 距离是指球从起始位置 ( 不包括 ) 到终点 ( 包括 ) 所经过的空地数。
# 你可以假设迷宫的边界都是墙 ( 见例子 )。
#
# Dijkstra算法，从起点开始，每次选择和已访问点距离最短的点访问，然后更新周围点的距离并把新发现的连接点加入queue。
# 由于queue记录了和已访问点连接的点，所以不需要visited。
# 当queue里的点的距离更新后，需要重新进入queue。而每次访问一个点的时候需要判断是不是距离更新过。如果更新过则跳过。
# 如果用dict来记录距离速度会大大下降。
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        record = [[inf] * n for _ in range(m)]

        record[start[0]][start[1]] = 0
        queue = []
        heappush(queue, (0, start[0], start[1]))
        while queue:
            dis, row, col = heappop(queue)
            if dis > record[row][col]:
                continue
            for dr, dc in dirs:
                nxrow, nxcol, steps = row, col, 0
                while 0 <= nxrow + dr < m and 0 <= nxcol + dc < n \
                        and maze[nxrow + dr][nxcol + dc] == 0:
                    nxrow += dr
                    nxcol += dc
                    steps += 1
                if record[nxrow][nxcol] > steps + dis:
                    record[nxrow][nxcol] = steps + dis
                    heappush(queue, (record[nxrow][nxcol], nxrow, nxcol))
        if record[destination[0]][destination[1]] < inf:
            return record[destination[0]][destination[1]]
        else:
            return -1
