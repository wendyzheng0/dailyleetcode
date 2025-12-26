###
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
#
# 动态规划。f[i][j]表示text1[:i+1]和text2[:j+1]的最长公共子序列长度。
# 如果text1[i] == text2[j]，则f[i][j] = f[i - 1][j - 1] + 1。
# 否则f[i][j] = max(f[i - 1][j], f[i][j - 1])。
# 最后返回f[n1 - 1][n2 - 1]。
# 本来还以为这样O(mn)的复杂度会超时，结果居然过了。
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        # f[i][j] is the longest subsequence of text1[:i+1] text2[:j+1]
        f = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        # 1. when text1[i] == text2[j], f[i][j] = f[i - 1][j - 1] + 1
        # 2. when text1[i] != text2[j], f[i][j] = max(f[i - 1][j], f[i][j - 1])
        for i in range(n1):
            for j in range(n2):
                if text1[i] == text2[j]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        return f[n1 - 1][n2 - 1]
