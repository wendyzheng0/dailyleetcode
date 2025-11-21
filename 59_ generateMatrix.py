from typing import List


###
# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
# 按顺序填充，遇到边界或已填过的就换方向。
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        i = j = d = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v = 1
        while v <= n * n:
            res[i][j] = v
            v += 1
            if v > n * n:
                break
            ii = i + dirs[d][0]
            jj = j + dirs[d][1]
            if 0 <= ii < n and 0 <= jj < n and res[ii][jj] == 0:
                i = ii
                j = jj
            else:
                d = (d + 1) % 4
                i += dirs[d][0]
                j += dirs[d][1]
        return res
