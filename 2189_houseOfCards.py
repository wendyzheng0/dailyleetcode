###
# 给你一个整数 n，代表你拥有牌的数量。一个 纸牌屋 满足以下条件:
# 一个 纸牌屋 由一行或多行 三角形 和水平纸牌组成。
# 三角形 是由两张纸牌相互靠在一起形成的。
# 一张纸牌必须水平放置在一行中 所有相邻 的三角形之间。
# 比第一行高的任何三角形都必须放在前一行的水平纸牌上。
# 每个三角形都被放置在行中 最左边 的可用位置。
# 返回使用所有 n 张纸牌可以构建的不同纸牌屋的数量。如果存在一行两个纸牌屋包含不同数量的纸牌，那么两个纸牌屋被认为是不同的。
#
# 动态规划。最底层如果有x个三角形，那就需要3*x-1张牌。dp[i][j]表示最底层有<=i个三角形，总共j张牌的方案数。
# dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - (3 * i - 1)] if j >= 3 * i - 1 else 0)
class Solution:
    def houseOfCards(self, n: int) -> int:
        # max triangles in bottom line
        x = (n + 1) // 3
        # dp[i][j], num of methods when bottom line contains <= i triangles and totally j cards
        # dp[i][j] = dp[i - 1][j] + (dp[i - 1][j - (3 * i - 1)] if j >= 3 * i - 1 else 0)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, x + 1):
            y = i * 3 - 1
            for j in range(n, y - 1, -1):
                dp[j] = dp[j] + dp[j - y]
        return dp[n]
