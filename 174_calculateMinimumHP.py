from typing import List
from math import inf


###
# 恶魔们抓住了公主并将她关在了地下城 dungeon 的 右下角 。地下城是由 m x n 个房间组成的二维网格。我们英勇的骑士最初被安置在 左上角 的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 为了尽快解救公主，骑士决定每次只 向右 或 向下 移动一步。
# 返回确保骑士能够拯救到公主所需的最低初始健康点数。
# 注意：任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
#
# 如果从左上角开始遍历，当前格子值大于0时，最小健康点数取决于左边和上面格子的最小健康点数。但当格子值小于0时，最小健康点数就同时需要判断路径和最小健康点数。
# 例如最后一个case，格子（1，2）值为0，从（0，2）过来的路径和为1，最小健康值为3，从（1，1）过来的路径和为-1，最小健康值为2。如果选择了（1，1）的路径，
# 那么达到（2，2）的最小健康值为5，而选择（0，2）的路径时只需要值需要最小健康值3.所有没有办法根据左边和上面的路径值和最小健康值确定当前格子应该选择的路径。
# 如果从右下角开始遍历，当我们知道了右边格子和下面格子需要的最小健康值，那我们就可以确定选择健康值小的路径。
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[inf] * n for _ in range(m)]
        # before you enter dungeon[i][j], you must get path value dp[i][j] to arrive end
        dp[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                low = inf
                if i < m - 1:
                    low = min(low, dp[i + 1][j])
                if j < n - 1:
                    low = min(low, dp[i][j + 1])
                dp[i][j] = max(1, low - dungeon[i][j])
        # print(dp)
        return dp[0][0]

if __name__ == "__main__":
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    print(Solution().calculateMinimumHP(dungeon))  # 7
    dungeon = [[0]]
    print(Solution().calculateMinimumHP(dungeon))  # 1
    dungeon = [[100]]
    print(Solution().calculateMinimumHP(dungeon))  # 1
    dungeon = [[1, -3, 3],[0, -2, 0],[-3, -3, -3]]
    print(Solution().calculateMinimumHP(dungeon))  # 3