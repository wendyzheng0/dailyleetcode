from typing import List


###
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 开始的时候记录每个位置左边的1的个数，然后遍历每个位置，如果当前位置为1，则向上求当前位置作为右下角的时候的最大矩形面积。
# 这个方法复杂度是O(rows * cols^2)。
# 后来看到别的解法统计每一行作为矩阵的底时，可以获得的最大矩阵面积。每个位置往上数的最多1的个数是遍历的时候更新的。
# 遍历每个位置的时候，如果前一个位置有比当前位置更多的1，则计算以他为高所能获得的最大矩形面积。这个矩形的底是更早的比他
# 矮的位置+1到当前位置-1.直到栈末尾的位置高度比当前位置低。
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        height = [0] * (cols + 1)
        res = 0
        for i in range(rows):
            q = [[-1, 0]]
            for j in range(cols + 1):
                if j < cols and matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
                while q and q[-1][1] > height[j]:
                    idx, h = q.pop()
                    s = (j - 1 - (q[-1][0] + 1) + 1) * h
                    # print(f"{i},{j}: pre: {s}, h:{h}, idx:{idx}")
                    res = max(res, s)
                q.append([j, height[j]])
            # print(height)
        return res

    def maximalRectangle1(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        left = [[0] * cols for _ in range(rows)]
        res = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    left[i][j] = left[i][j - 1] + 1
                    width = left[i][j]
                    for k in range(i, -1, -1):
                        if matrix[k][j] == 0:
                            break
                        width = min(width, left[k][j])
                        res = max(res, width * (i - k + 1))
            # print(left)
        return res
