from typing import List


###
# 给你一个正整数 n ，表示最初有一个 n x n 、下标从 0 开始的整数矩阵 mat ，矩阵中填满了 0 。
# 另给你一个二维整数数组 query 。针对每个查询 query[i] = [row1i, col1i, row2i, col2i] ，请你执行下述操作：
# 找出 左上角 为 (row1i, col1i) 且 右下角 为 (row2i, col2i) 的子矩阵，将子矩阵中的 每个元素 加 1 。也就是给所有满足 row1i <= x <= row2i 和 col1i <= y <= col2i 的 mat[x][y] 加 1 。
# 返回执行完所有操作后得到的矩阵 mat 。
#
# 看提示写了个一维的查分数组rangeAddQueries1，虽然过了但速度很慢。学习了快速的解法改成了二维的查分数组rangeAddQueries，速度马上上来了。
# 关键在于需要分别记录行和列的查分，而还原的时候行和列需要分开来算。第(i, j)个元素的值是查分数组的第i行前缀和加上第j列的前缀和，而不能简单的用（i-1，j）和（i，j-1）的元素。
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            res[row1][col1] += 1
            if col2 + 1 < n:
                res[row1][col2 + 1] -= 1
            if row2 + 1 < n:
                res[row2 + 1][col1] -= 1
                if col2 + 1 < n:
                    res[row2 + 1][col2 + 1] += 1
        for i in range(n):
            acc = 0
            for j in range(n):
                acc += res[i][j]
                res[i][j] = res[i - 1][j] + acc if i >= 1 else acc
        return res

    def rangeAddQueries1(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        for row1, col1, row2, col2 in queries:
            for i in range(row1, row2 + 1):
                res[i][col1] += 1
                if col2 + 1 < n:
                    res[i][col2 + 1] -= 1
        for i in range(n):
            for j in range(1, n):
                res[i][j] += res[i][j - 1]
        return res
