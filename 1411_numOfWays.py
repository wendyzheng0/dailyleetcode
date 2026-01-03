from functools import cache


###
# 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
# 给你网格图的行数 n 。
# 请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。
#
# 记忆化搜索，先找出每行可以填的合法颜色组合cand，然后递归统计合法的涂色方案数。
class Solution:
    def numOfWays(self, n: int) -> int:
        cand = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                cand.append((i, j, 3 - i - j))
                cand.append((i, j, i))
        # print(cand)
        MOD = 1_000_000_007

        @cache
        def dfs(n, pre):
            if n == 0:
                return 1
            res = 0
            for cur in cand:
                if pre[0] == cur[0] or pre[1] == cur[1] or pre[2] == cur[2]:
                    continue
                res = (res + dfs(n - 1, cur)) % MOD
            return res
        return dfs(n, (-1, -1, -1))
