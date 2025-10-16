from typing import List


####
# 给你一个 n x n 的方形整数数组matrix，请你找出并返回通过matrix的下降路径的最小和 。
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素
# 和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
# 具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。
#
# 这里使用动态规划，pre数组表示上一行的最小路径和，cur数组表示当前行的最小路径和。
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        pre = [0] * n
        cur = [0] * n
        for i in range(n):
            for j in range(1, n - 1):
                cur[j] = min(pre[j - 1], pre[j], pre[j + 1]) + matrix[i][j]
            cur[0] = min(pre[0], pre[1 % n]) + matrix[i][0]
            cur[n - 1] = min(pre[n - 1], pre[(n - 2) % n]) + matrix[i][n - 1]
            pre, cur = cur, pre
        return min(pre)
