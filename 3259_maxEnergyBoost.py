from typing import List


###
# 来自未来的体育科学家给你两个整数数组 energyDrinkA 和 energyDrinkB，数组长度都等于 n。这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。
# 你需要每小时饮用一种能量饮料来 最大化 你的总强化能量。然而，如果从一种能量饮料切换到另一种，你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。
# 返回在接下来的 n 小时内你能获得的 最大 总强化能量。
# 注意 你可以选择从饮用任意一种能量饮料开始。
#
# 动态规划。dp[i][0]代表第i小时喝A饮料的最大能量，dp[i][1]代表第i小时喝B饮料的最大能量。
# dp[i][0]可以分为换和不换的情况。换的情况为dp[i-2][1] + energyDrinkA[i]，不换的情况为dp[i-1][0] + energyDrinkA[i]。
# dp[i][1]同理。最后返回max(dp[n-1][0], dp[n-1][1], dp[n-2][0], dp[n-2][1])。
# 由于只跟最后4个元素相关，可以优化为4个变量。
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        prea = a = preb = b = 0
        n = len(energyDrinkA)
        for i in range(n):
            newa = max(a + energyDrinkA[i], preb + energyDrinkA[i])
            newb = max(b + energyDrinkB[i], prea + energyDrinkB[i])
            prea, preb = a, b
            a, b = newa, newb
        return max(prea, preb, a, b)

    def maxEnergyBoost1(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # dp[i]=[a,b]
        # a: max energy when drinking A in i hour
        # b: max energy when drinking B in i hour
        # dp[i][0] = max(dp[i-1][0] + energyDrinkA[i], dp[i-2][1] + energyDrinkA[i])
        # dp[i][1] = max(dp[i-1][1] + energyDrinkB[i], dp[i-2][0] + energyDrinkB[i])
        n = len(energyDrinkA)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            dp[i][0] = max(dp[i - 1][0] + energyDrinkA[i], dp[i - 2][1] + energyDrinkA[i])
            dp[i][1] = max(dp[i - 1][1] + energyDrinkB[i], dp[i - 2][0] + energyDrinkB[i])
        return max([*dp[n - 1], *dp[n - 2]])
