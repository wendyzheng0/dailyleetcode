from typing import List


###
# 给你一个 m x n 的二进制网格 grid，其中：
# * grid[i][j] == 0 表示一个空格子。
# * grid[i][j] == 1 表示一面镜子。
# 一个机器人从网格的左上角 (0, 0) 出发，想要到达右下角 (m - 1, n - 1)。它只能向 右 或向 下 移动。如果机器人试图移入一个有镜子的格子，它会在进入该格子前被 反射：
# 如果它试图向 右 移动进入镜子，它会被转向 下 方，并移动到镜子正下方的格子里。
# 如果它试图向 下 移动进入镜子，它会被转向 右 方，并移动到镜子正右方的格子里。
# 如果这次反射会导致机器人移动到网格边界之外，则该路径被视为无效，不应被计数。
# 返回从 (0, 0) 到 (m - 1, n - 1) 不同的有效路径数量。
# 由于答案可能非常大，请将其返回对 109 + 7 取模 的结果。
# 注意：如果一次反射将机器人移动到一个有镜子的格子，机器人会立即再次被反射。这次反射的方向取决于它进入该镜子的方向：如果它是向右移动进入的，它将被转向下方；如果它是向下移动进入的，它将被转向右方。
#
# 常规做法，记录到达每个格子的路径数，对于镜子格子，需要记录可以往右走的路径数和往下走的路径数，然后根据方向累加。
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 1_000_000_007
        m, n = len(grid), len(grid[0])
        pre = [0] * n
        cur = [0] * n
        pre[0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur[j] = [0, 0]
                    if i > 0:
                        if grid[i - 1][j] == 1:
                            cur[j][0] = pre[j][1]
                        else:
                            cur[j][0] = pre[j]
                    if j > 0:
                        if grid[i][j - 1] == 1:
                            cur[j][1] = cur[j - 1][0]
                        else:
                            cur[j][1] = cur[j - 1]
                    continue
                if i > 0 and grid[i - 1][j] == 1:
                    cur[j] = pre[j][1]
                else:
                    cur[j] = pre[j]
                if j > 0:
                    if grid[i][j - 1] == 1:
                        cur[j] += cur[j - 1][0]
                    else:
                        cur[j] += cur[j - 1]
                cur[j] = cur[j] % MOD
            pre, cur = cur, pre
            # print(pre)
        return pre[-1]