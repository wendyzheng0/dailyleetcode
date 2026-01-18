from typing import List
from heapq import heappop, heappush
import copy
from math import inf


###
# 由空地和墙组成的迷宫中有一个球。球可以向上（u）下（d）左（l）右（r）四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向（必须与上一个选择的方向不同）。迷宫中还有一个洞，当球运动经过洞时，就会掉进洞里。
# 给定球的起始位置，目的地和迷宫，找出让球以最短距离掉进洞里的路径。 距离的定义是球从起始位置（不包括）到目的地（包括）经过的空地个数。通过'u', 'd', 'l' 和 'r'输出球的移动方向。 由于可能有多条最短路径， 请输出字典序最小的路径。如果球无法进入洞，输出"impossible"。
# 迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。
#
# 类似于dijistra算法，利用堆优化搜索过程。从起点开始，每次从相邻的点里面选最近的点访问。如果遇到终点，更新最短路径，并继续搜索。
# 如果选择的点访问过就跳过。如果选择的点距离大于已知的最短距离，或者距离相同但路径字典序更大，就跳过。
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])

        def move(x, y, dx, dy):
            distance = 0
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] != 1:
                distance += 1
                x += dx
                y += dy
                if x == hole[0] and y == hole[1]:
                    break
            return [x, y, distance]

        DIRS = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]
        minstep = inf
        minpath = 'z'
        candidates = [[0, ball[0], ball[1], '']]
        mindist = dict({(ball[0], ball[1]): 0})
        visited = set()
        while len(candidates) > 0:
            d, x, y, p = heappop(candidates)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if d > minstep or d > mindist[(x, y)]:
                continue
            for dx, dy, pp in DIRS:
                xx, yy, dd = move(x, y, dx, dy)
                if (xx, yy) in visited:
                    continue
                s = d + dd
                path = p + pp
                if xx == hole[0] and yy == hole[1]:
                    if minstep > s or (minstep == s and path < minpath):
                        minstep = s
                        minpath = path
                mindist[(xx, yy)] = min(mindist.get((xx, yy), inf), s)
                heappush(candidates, (s, xx, yy, path))
            # print(candidates)
        return minpath if minpath != 'z' else 'impossible'
