###
# 这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。
# 给定三个整数 n、k 和 target，请返回投掷骰子的所有可能得到的结果（共有 kn 种方式），使得骰子面朝上的数字总和等于 target。
# 由于答案可能很大，你需要对 109 + 7 取模。
#
# 动态规划，f[i][j]表示投掷i个骰子得到j的方案数。f[i][j] = sum(f[i-1][j-x]) 1<=x<=k。
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # f[i][j]: number of ways to get sum j when have i dice
        # f[i][j] = sum(f[i-1][j-x]) 1<=x<=k
        MOD = 1_000_000_007
        f = [0] + [1] * k + [0] * (target - k)
        for i in range(n - 1):
            for j in range(target, -1, -1):
                f[j] = sum(f[max(j - k, 0):j]) % MOD
            # print(f"{i}:{g}")
        return f[target]
