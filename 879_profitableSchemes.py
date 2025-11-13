from typing import List


###
# 集团里有 n 名员工，他们可以完成各种各样的工作创造利润。
# 第 i 种工作会产生 profit[i] 的利润，它要求 group[i] 名成员共同参与。如果成员参与了其中一项工作，就不能参与另一项工作。
# 工作的任何至少产生 minProfit 利润的子集称为 盈利计划 。并且工作的成员总数最多为 n 。
# 有多少种计划可以选择？因为答案很大，所以 返回结果模 10^9 + 7 的值。
#
# 这个题和背包问题很像，但不会写，自己写尝试记录每种不超过minProfit的方案和已经满足minProfit的方案还有的空位数。毫不疑问
# 超过内存了。看了官方解答，学着用二维dp来记录，这样记录的东西就少很多，计算也快很多。
# 当遍历到第i个项目的时候，dp[j][k]表示前面i-1个项目中，使用j个员工，至少产生k利润的盈利计划的数目。
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[1] + [0] * minProfit for _ in range(n + 1)]
        for i in range(len(group)):
            for j in range(n, group[i] - 1, -1):
                # dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-group[i]][max(k-profit[i], 0)]
                for k in range(minProfit, -1, -1):
                    dp[j][k] += dp[j - group[i]][max(k - profit[i], 0)]
        return dp[n][minProfit] % 1_000_000_007


if __name__ == "__main__":
    solution = Solution()
    print(solution.profitableSchemes(5, 3, [2,2], [2,3]))  # Expected: 2
    print(solution.profitableSchemes(10, 5, [2,3,5], [6,7,8]))  # Expected: 7
    print(solution.profitableSchemes(64, 0, [80, 40], [88, 88]))  # Expected: 2
    print(solution.profitableSchemes(100, 10, [66,24,53,49,86,37,4,70,99,68,14,91,70,71,70,98,48,26,13,86,4,82,1,7,51,37,27,87,2,65,93,66,99,28,17,93,83,91,45,3,59,87,92,62,77,21,9,37,11,4,69,46,70,47,28,40,74,47,12,3,85,16,91,100,39,24,52,50,40,23,64,22,2,15,18,62,26,76,3,60,64,34,45,40,49,11,5,8,40,71,12,60,3,51,31,5,42,52,15,36], [8,4,8,8,9,3,1,6,7,10,1,10,4,9,7,11,5,1,7,4,11,1,5,9,9,5,1,10,0,10,4,1,1,1,6,9,3,6,2,5,4,7,8,5,2,3,0,6,4,5,9,9,10,7,1,8,9,6,0,2,9,2,2,8,6,10,3,4,6,1,10,7,5,4,8,1,8,5,5,4,1,1,10,0,8,0,1,11,5,4,7,9,1,11,1,0,1,6,8,3]))  # Expected: 188883405
