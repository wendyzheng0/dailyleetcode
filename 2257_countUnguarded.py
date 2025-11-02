from typing import List


###
# 给你两个整数 m 和 n 表示一个下标从 0 开始的 m x n 网格图。同时给你两个二维整数数组 guards 和 walls ，其中 guards[i] = [rowi, coli] 且 walls[j] = [rowj, colj] ，分别表示第 i 个警卫和第 j 座墙所在的位置。
# 一个警卫能看到 4 个坐标轴方向（即东、南、西、北）的 所有 格子，除非他们被一座墙或者另外一个警卫 挡住 了视线。如果一个格子能被 至少 一个警卫看到，那么我们说这个格子被 保卫 了。
# 请你返回空格子中，有多少个格子是 没被保卫 的。
#
# 标记受保护的格子：遍历每个警卫，然后向四个方向遍历，如果遇到墙或者另一个警卫，则停止遍历。
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        bitmap = [[0] * n for _ in range(m)]
        for x, y in walls:
            bitmap[x][y] = 1
        for x, y in guards:
            bitmap[x][y] = 1
        for x, y in guards:
            for xx in range(x + 1, m):
                if bitmap[xx][y] == 1:
                    break
                bitmap[xx][y] = 2
            for xx in range(x - 1, -1, -1):
                if bitmap[xx][y] == 1:
                    break
                bitmap[xx][y] = 2
            for yy in range(y + 1, n):
                if bitmap[x][yy] == 1:
                    break
                bitmap[x][yy] = 2
            for yy in range(y - 1, -1, -1):
                if bitmap[x][yy] == 1:
                    break
                bitmap[x][yy] = 2
        res = 0
        for x in range(m):
            for y in range(n):
                res += 1 if bitmap[x][y] == 0 else 0
        return res
