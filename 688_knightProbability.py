from functools import cache


###
# 在一个 n x n 的国际象棋棋盘上，一个骑士从单元格 (row, column) 开始，并尝试进行 k 次移动。行和列是 从 0 开始 的，所以左上单元格是 (0,0) ，右下单元格是 (n - 1, n - 1) 。
# 象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。
# 每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。
# 骑士继续移动，直到它走了 k 步或离开了棋盘。
# 返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。
#
# 记忆化搜索，统计从row，column出发经过k步之后还在棋盘上的路径数目。总路径数是8^k。
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        @cache
        def dfs(steps, x, y):
            if steps == 0:
                return 1
            res = 0
            for dx, dy in dirs:
                if 0 <= dx + x < n and 0 <= dy + y < n:
                    res += dfs(steps - 1, dx + x, dy + y)
            # print(f"{steps}, {x}, {y}: {res}")
            return res
        paths = dfs(k, row, column)
        # print(paths)
        return paths / (8 ** k)
