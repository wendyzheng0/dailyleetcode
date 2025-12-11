from typing import List
from math import inf


###
# 给你一个正整数 n，表示一个 n x n 的城市，同时给定一个二维数组 buildings，其中 buildings[i] = [x, y] 表示位于坐标 [x, y] 的一个 唯一 建筑。
# 如果一个建筑在四个方向（左、右、上、下）中每个方向上都至少存在一个建筑，则称该建筑 被覆盖 。
# 返回 被覆盖 的建筑数量。
#
# 记录每个建筑在四个方向上的最小和最大y坐标，然后遍历每个建筑，如果该建筑在四个方向上的最小和最大y坐标都小于该建筑的y坐标，则该建筑被覆盖。
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row = [[inf, -inf] for _ in range(n + 1)]
        col = [[inf, -inf] for _ in range(n + 1)]
        for x, y in buildings:
            row[x][0] = min(row[x][0], y)
            row[x][1] = max(row[x][1], y)
            col[y][0] = min(col[y][0], x)
            col[y][1] = max(col[y][1], x)
        res = 0
        for x, y in buildings:
            if row[x][0] < y < row[x][1] and col[y][0] < x < col[y][1]:
                res += 1
        return res
