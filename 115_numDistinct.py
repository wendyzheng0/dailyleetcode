###
# 给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数。
# 测试用例保证结果在 32 位有符号整数范围内。
#
# 用动态规划解决。dp[i][j] 表示 t[:i] 在 s[:j] 中出现的次数。那么
# 当t[i] == s[j]时，dp[i][j] = dp[i-1][j-1] + dp[i][j-1]，否则dp[i][j] = dp[i][j-1]。
# 初始化：dp[0][j] 为t[0]在s[:j]中出现的次数。
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns, nt = len(s), len(t)
        # dp[i][j]: num of t[:i] occurs in s[:j]
        # = dp[i][j-1] + (dp[i-1][j-1] if t[i] == s[j] else 0)
        # dp[0][j] = num of t[0] in s[:j]
        dp = [0] * ns + [0]
        cur = [0] * ns + [0]
        for j in range(ns):
            dp[j] = dp[j - 1]
            if t[0] == s[j]:
                dp[j] += 1
        # print(dp)
        for i in range(1, nt):
            for j in range(ns):
                cur[j] = cur[j - 1]
                if t[i] == s[j]:
                    cur[j] += dp[j - 1]
            dp, cur = cur, dp
            # print(dp)
        return dp[ns - 1]
