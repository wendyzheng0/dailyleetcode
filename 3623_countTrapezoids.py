from typing import List
from collections import Counter


###
# 给你一个二维整数数组 points，其中 points[i] = [xi, yi] 表示第 i 个点在笛卡尔平面上的坐标。
# 水平梯形 是一种凸四边形，具有 至少一对 水平边（即平行于 x 轴的边）。两条直线平行当且仅当它们的斜率相同。
# 返回可以从 points 中任意选择四个不同点组成的 水平梯形 数量。
# 由于答案可能非常大，请返回结果对 109 + 7 取余数后的值。
#
# 统计每个y坐标上点的数量，然后遍历每个y坐标，计算该坐标上每两个点的组合数，然后乘以之前坐标上所有的组合数就是
# 该坐标为底边时可以组成的水平梯形数。全部累加得到结果。
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1_000_000_007
        # ygroup = defaultdict(int)
        # for x, y in points:
        #     ygroup[y] += 1
        # print(ygroup)
        ygroup = Counter(y for x, y in points).values()
        # comgroup = [v * (v - 1) // 2 for k, v in ygroup.items() if v > 1]
        # print(comgroup)
        # n = len(comgroup)
        res = 0
        s = 0
        # for i in range(n):
        #     res = (res + comgroup[i] * s)
        #     s += comgroup[i]
        for c in ygroup:
            t = c * (c - 1) // 2
            res = (res + t * s) % MOD
            s += t
        return res % MOD
