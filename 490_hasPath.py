from typing import List


###
# 由空地（用 0 表示）和墙（用 1 表示）组成的迷宫 maze 中有一个球。球可以途经空地向 上、下、左、右 四个方向滚动，且在遇到墙壁前不会停止滚动。当球停下时，可以选择向下一个方向滚动。
# 给你一个大小为 m x n 的迷宫 maze ，以及球的初始位置 start 和目的地 destination ，其中 start = [startrow, startcol] 且 destination = [destinationrow, destinationcol] 。请你判断球能否在目的地停下：如果可以，返回 true ；否则，返回 false 。
# 你可以 假定迷宫的边缘都是墙壁（参考示例）。
#
# 用深度优先搜索，从起点开始，每次选择一个方向滚动确定下一个停止点，如果停止点曾经到过则跳过（因为每个停止点可以看作是一个新的起点），如果到达终点则直接返回。
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            visited[i][j] = True
            for x, y in dirs:
                ii, jj = i, j
                while 0 <= ii + x < m and 0 <= jj + y < n and maze[ii + x][jj + y] != 1:
                    ii += x
                    jj += y
                if not visited[ii][jj] and dfs(ii, jj):
                    return True
            return False

        return dfs(*start)
