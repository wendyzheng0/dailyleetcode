from typing import List


###
# 给你一个 m x n 的网格。一个机器人从网格的左上角 (0, 0) 出发，目标是到达网格的右下角 (m - 1, n - 1)。在任意时刻，机器人只能向右或向下移动。
# 网格中的每个单元格包含一个值 coins[i][j]：
# 如果 coins[i][j] >= 0，机器人可以获得该单元格的金币。
# 如果 coins[i][j] < 0，机器人会遇到一个强盗，强盗会抢走该单元格数值的 绝对值 的金币。
# 机器人有一项特殊能力，可以在行程中 最多感化 2个单元格的强盗，从而防止这些单元格的金币被抢走。
# 注意：机器人的总金币数可以是负数。
# 返回机器人在路径上可以获得的 最大金币数 。
#
# 记录到达每个格子时，使用0，1, 2次特殊能力的所能获得的最大金币数。想必没有特殊能力的情况多了两个变量。
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        cost = [[0] * 3 for _ in range(n)]
        cost[0][0] = coins[0][0]
        for j in range(1, n):
            cost[j][0] = cost[j - 1][0] + coins[0][j]
            cost[j][1] = max(cost[j - 1][0], cost[j - 1][1] + coins[0][j])
            cost[j][2] = max(cost[j - 1][1], cost[j - 1][2] + coins[0][j])
        # print(cost)
        cur = [[0] * 3 for _ in range(n)]
        for i in range(1, m):
            cur[0][0] = cost[0][0] + coins[i][0]
            cur[0][1] = max(cost[0][0], cost[0][1] + coins[i][0])
            cur[0][2] = max(cost[0][1], cost[0][2] + coins[i][0])
            for j in range(1, n):
                cur[j][0] = max(cost[j][0], cur[j - 1][0]) + coins[i][j]
                cur[j][1] = max(cost[j][0], cur[j - 1][0], cost[j][1] + coins[i][j], cur[j - 1][1] + coins[i][j])
                cur[j][2] = max(cost[j][1], cur[j - 1][1], cost[j][2] + coins[i][j], cur[j - 1][2] + coins[i][j])
            cost, cur = cur, cost
            # print(cost)
        return max(cost[-1])
