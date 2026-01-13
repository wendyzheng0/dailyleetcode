from typing import List
from collections import defaultdict
from itertools import pairwise


###
# 给你一个二维整数数组 squares ，其中 squares[i] = [xi, yi, li] 表示一个与 x 轴平行的正方形的左下角坐标和正方形的边长。
# 找到一个最小的 y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 等于 该线以下正方形的总面积。
# 答案如果与实际答案的误差在 10-5 以内，将视为正确答案。
# 注意：正方形 可能会 重叠。重叠区域应该被 多次计数 。
#
# 开始的时候用二分法从最小的y和最大的y之间找到答案（separateSquares1），但是每个y都需要计算一次y下面的面积，比较慢。
# 后来看到别的解法把正方形按照水平边分成多块，每块的面积相当于覆盖在这个区间的正方形边长和乘以该块的高度。
# 这样就可以累加计算某个y下面的面积，当面积大于等于总面积的一半时，目标的y就可以通过比例计算出来。
# curS - curL * (y1 - y) = totalarea / 2，解出y = y1 - (curS * 2 - totalarea) / (curL * 2)
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 把正方形按照边划分成多个矩形，用差分数组记录每个y对应的矩形的底边之和
        diff = defaultdict(int)
        for x, y, l in squares:
            diff[y] += l
            diff[y + l] -= l
        totalarea = sum(l * l for _, _, l in squares)
        curL = curS = 0
        for y, y1 in pairwise(sorted(diff)):
            curL += diff[y]
            curS += curL * (y1 - y)
            if curS * 2 >= totalarea:
                return y1 - (curS * 2 - totalarea) / (curL * 2)
        return -1

    def separateSquares1(self, squares: List[List[int]]) -> float:
        bounds = [[y, y + l, l, l * l] for x, y, l in squares]
        bounds.sort(key=lambda x: (x[1], x[0]))
        lower = min(bounds, key=lambda x: x[0])[0]
        upper = max(bounds, key=lambda x: x[1])[1]
        target = sum(l * l for x, y, l in squares) / 2
        while upper - lower >= 0.00001:
            mid = (lower + upper) / 2
            area = 0
            for y1, y2, l, s in bounds:
                if mid >= y2:
                    area += s
                elif mid > y1:
                    area += (mid - y1) * l
                if area >= target:
                    break
            # print(f"({lower},{upper}), mid:{mid}, area:{area}")
            if area >= target:
                upper = mid
            elif area < target:
                lower = mid
        return lower
