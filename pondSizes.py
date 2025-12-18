from typing import List


###
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
# 示例：
# 输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]
#
# 深度优先搜索，遍历每个点，如果点为0，则以该点为起点，深度优先搜索，记录搜索到的水域的面积。没想到用循环的方式还没有用递归快。主要是因为维护待访问的点比较耗时。
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        ans = []
        m, n = len(land), len(land[0])

        def dfs(x, y):
            land[x][y] = 1
            res = 1
            for dx, dy in dirs:
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and land[xx][yy] == 0:
                    res += dfs(xx, yy)
            return res

        for i in range(m):
            for j in range(n):
                if land[i][j] == 0:
                    ans.append(dfs(i, j))
        return sorted(ans)
    
    def pondSizes1(self, land: List[List[int]]) -> List[int]:
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        res = []
        m, n = len(land), len(land[0])
        for i in range(m):
            for j in range(n):
                if land[i][j] != 0:
                    continue
                pool = set({(i, j)})
                size = 0
                while pool:
                    for x, y in list(pool):
                        pool.remove((x, y))
                        land[x][y] = 1
                        size += 1
                        for dx, dy in dirs:
                            xx, yy = x + dx, y + dy
                            if 0 <= xx < m and 0 <= yy < n and land[xx][yy] == 0:
                                pool.add((xx, yy))
                res.append(size)
        return sorted(res)
