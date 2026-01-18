from typing import List
import copy


###
# 一个 k x k 的 幻方 指的是一个 k x k 填满整数的方格阵，且每一行、每一列以及两条对角线的和 全部相等 。幻方中的整数 不需要互不相同 。显然，每个 1 x 1 的方格都是一个幻方。
# 给你一个 m x n 的整数矩阵 grid ，请你返回矩阵中 最大幻方 的 尺寸 （即边长 k）。
#
# 从大到小遍历可能取的幻方边长，对于每个边长，遍历所有可能的左上角位置，检查是否满足幻方条件。利用前缀和优化检查过程。
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hsum = copy.deepcopy(grid)
        vsum = copy.deepcopy(grid)
        for i in range(m):
            for j in range(1, n):
                hsum[i][j] += hsum[i][j - 1]
            hsum[i] = hsum[i] + [0]
        # print(f"hsum:{hsum}")
        for j in range(n):
            for i in range(1, m):
                vsum[i][j] += vsum[i - 1][j]
        vsum.append([0] * n)
        # print(f"vsum:{vsum}")
        for width in range(min(m, n), 1, -1):
            for i in range(m - width + 1):
                for j in range(n - width + 1):
                    target = hsum[i][j + width - 1] - hsum[i][j - 1]
                    # print(f"width:{width}, point ({i}, {j}), target={target}")
                    d1 = d2 = 0
                    for k in range(width):
                        if hsum[k + i][j + width - 1] - hsum[k + i][j - 1] != target \
                                or vsum[i + width - 1][j + k] - vsum[i - 1][j + k] != target:
                            # print(f"not working when k={k}")
                            break
                        d1 += grid[i + k][j + k]
                        d2 += grid[i + k][j + width - k - 1]
                    else:
                        if d1 == d2 == target:
                            return width
                        # print("not working")
        return 1
