from typing import List


###
# 3 x 3 的幻方是一个填充有 从 1 到 9  的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
# 给定一个由整数组成的row x col 的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？
# 注意：虽然幻方只能包含 1 到 9 的数字，但 grid 可以包含最多15的数字。
#
# 开始没注意到最大行列小于等于10，写了一个很复杂的算法，结果后来发现暴力算最快。
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(i, j):
            d = [False] * 10
            colsum = [0] * 3
            for p in range(i, i + 3):
                rowsum = 0
                for q in range(j, j + 3):
                    if grid[p][q] > 9 or d[grid[p][q]]:
                        return False
                    d[grid[p][q]] = True
                    colsum[q - j] += grid[p][q]
                    rowsum += grid[p][q]
                if rowsum != 15:
                    return False
            if any(v != 15 for v in colsum):
                return False
            n1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
            n2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
            return n1 == n2 == 15

        res = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if check(i, j):
                    res += 1
        return res

    def numMagicSquaresInside1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3:
            return 0
        rowsum = [[sum(grid[i][j:j+3]) for j in range(n - 2)] for i in range(m)] # m*(n-2)
        colsum = [[0] * n for _ in range(m - 2)] # (m-2)*n
        for j in range(n):
            for i in range(m - 2):
                colsum[i][j] = sum(grid[k][j] for k in range(i, i + 3))
        # print(rowsum)
        # print(colsum)
        res = 0
        i = j = 0
        forward = True

        def getinvalidpos(i, j):
            d = [0] * 10
            for ii in range(i, i + 3):
                for jj in range(j, j + 3):
                    if grid[ii][jj] > 9:
                        invalidi = ii
                        invalidj = jj
                        return (invalidi, invalidj), d
                    d[grid[ii][jj]] += 1
            return None, d

        def getnextpos(forward, i, j, invalidpos):
            while i < m - 2 and j < n - 2:
                if forward:
                    if j == n - 3:
                        if i == m - 3:
                            return (forward, m, n)
                        i += 1
                        forward = False
                    else:
                        j += 1
                else:
                    if j == 0:
                        if i == m - 3:
                            return (forward, m, n)
                        i += 1
                        forward = True
                    else:
                        j -= 1
                if invalidpos is None or not (i <= invalidpos[0] < i + 3 and j <= invalidpos[1] < j + 3):
                    break
                # print(f"{i},{j}")
            return (forward, i, j)

        while i < m - 2 and j < n - 2:
            invalidpos, d = getinvalidpos(i, j)
            # print(f"{i},{j}, d:{d}, invalidpos:{invalidpos}")
            if invalidpos is None or not (i <= invalidpos[0] < i + 3 and j <= invalidpos[1] < j + 3):
                # print(f"{i},{j}")
                if 15 == rowsum[i][j] == rowsum[i + 1][j] == rowsum[i + 2][j] == colsum[i][j] == colsum[i][j + 1] == colsum[i][j + 2] == (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]) == (grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]):
                    if all(v == 1 for v in d[1:]):
                        res += 1
            forward, i, j = getnextpos(forward, i, j, invalidpos)


        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]])) # 1
    print(solution.numMagicSquaresInside1([[8]])) # 0
    print(solution.numMagicSquaresInside([[5,5,5],[5,5,5],[5,5,5]])) # 0
    print(solution.numMagicSquaresInside1([[10,3,5],[1,6,11],[7,9,2]])) # 0
    print(solution.numMagicSquaresInside([[4,10,1,6],[2,5,8,5],[9,0,6,4],[1,7,2,9]])) # 0
    print(solution.numMagicSquaresInside1([[3,2,9,2,7],[6,1,8,4,2],[7,5,3,2,7],[2,9,4,9,6],[4,3,8,2,5]])) # 1
