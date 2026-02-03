###
# 给定一个二维矩阵 matrix，以下类型的多个请求：
# 计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
# 实现 NumMatrix 类：
# NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
# int sumRegion(int row1, int col1, int row2, int col2) 返回 左上角 (row1, col1) 、右下角 (row2, col2) 所描述的子矩阵的元素 总和 。
#
# 用前缀和加速计算，matrix[i][j]表示左上角是[0][0],右下角是[i][j]的矩阵和。
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.data = matrix
        m, n = len(matrix), len(matrix[0])
        for j in range(1, n):
            matrix[0][j] += matrix[0][j - 1]
        for i in range(1, m):
            matrix[i][0] += matrix[i - 1][0]
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1] + matrix[i - 1][j] - matrix[i - 1][j - 1]
        # print(self.data)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.data[row2][col2] - (self.data[row2][col1 - 1] if col1 >= 1 else 0) \
            - (self.data[row1 - 1][col2] if row1 >= 1 else 0) \
            + (self.data[row1 - 1][col1 - 1] if row1 >= 1 and col1 >= 1 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)