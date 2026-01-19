from typing import List


###
# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
# 请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
#
# 利用前缀和优化计算区域和的过程, matsum[i][j] 表示从(0,0)到(i,j)的区域和。
# 开始的时候width从大到小尝试，遍历每个可能的左上角坐标，能过，但比较慢。
# 看了别的的解法改成从小到大尝试，每检查一个左上角坐标，width从上一次合法的width+1开始。
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        matsum = [[0] * (n + 1) for _ in range(m + 1)]
        if any(1 for row in mat for v in row if v <= threshold):
            minwidth = 1
        else:
            return 0
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                matsum[i][j] = matsum[i - 1][j] + matsum[i][j - 1] - matsum[i - 1][j - 1] + v
            # print(matsum[i])
        width = minwidth + 1
        for i in range(m):
            if i + width > m:
                break
            for j in range(n):
                if j + width > n:
                    break
                while width <= min(m, n):
                    if i + width - 1 >= m or j + width - 1 >= n:
                        break
                    s = matsum[i + width - 1][j + width - 1] \
                        - matsum[i - 1][j + width - 1] \
                        - matsum[i + width - 1][j - 1] + matsum[i - 1][j - 1]
                    if s <= threshold:
                        # print(f"{i}, {j}, width:{width}")
                        width += 1
                    else:
                        break
        return width - 1
