###
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
#
# 动态规划，dp[i][j] 表示 text1[:i+1]和 text2[:j+1]的最长公共子序列长度。用两个数组来节省存储，数组最后加了一个0用于处理边界情况。
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        #dp[i][j] = dp[i-1][j-1] + 1 when text1[i] == text2[j]
        #dp[i][j] = max(dp[i-1][j], dp[i][j-1]) when text1[i] != text2[j]
        dp = [0] * (n + 1)
        cur = [0] * (n + 1)
        for i in range(m):
            for j in range(n):
                v = max(dp[j], cur[j - 1])
                if text1[i] == text2[j]:
                    v = max(v, dp[j - 1] + 1)
                cur[j] = v
            dp, cur = cur, dp
            # print(dp)
        return dp[n - 1]
