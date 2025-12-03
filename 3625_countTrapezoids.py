from typing import List
from collections import defaultdict
from math import inf


###
# 给你一个二维整数数组 points，其中 points[i] = [xi, yi] 表示第 i 个点在笛卡尔平面上的坐标。
# 返回可以从 points 中任意选择四个不同点组成的梯形的数量。
# 梯形 是一种凸四边形，具有 至少一对 平行边。两条直线平行当且仅当它们的斜率相同。
#
# 这题比昨天的3623水平梯形难很多。普通梯形可以有多种斜率，所以增加了一维记录斜率。把所有点两两配对成线段，
# 然后按照斜率分组统计。相同斜率的线段如果截距也一样就是在同一直线上，没法形成四边形，所以不同截距的线段
# 可以组成一个梯形。这样的方法在统计平行四边形的时候会统计两遍，因为他有两对平行边。所以再减去平行四边形的
# 数量。平行四边形的对角线中点是重合的（这些对角线同时也是所有线段里面的线），但是线不能重合。所以按照线段
# 中点去分组，同一组里面斜率不一样的对角线可以组成一个平行四边形。这样就可以减去平行四边形的数量了。
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        pp = defaultdict(lambda: defaultdict(int))
        midpoint = defaultdict(lambda: defaultdict(int))
        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dx = x2 - x
                dy = y2 - y
                k = dy / dx if dx else inf
                b = (y * dx - x * dy) / dx if dx else x
                pp[k][b] += 1
                midpoint[(x + x2, y + y2)][k] += 1

        res = 0
        for group in pp.values():
            # same k
            s = 0
            for b, c in group.items():
                res += c * s
                s += c

        for mp in midpoint.values():
            # pair of points share same midpoint
            s = 0
            for k, c in mp.items():
                res -= c * s
                s += c
        return res
