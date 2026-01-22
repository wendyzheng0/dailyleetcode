###
# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
# 每步 可以删除任意一个字符串中的一个字符。
#
# 动态规划。类似求最长子序列问题。dp[i][j] 表示 word1[:i+1] 和 word2[:j+1] 相同所需的最小步数。
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] min steps to make word1[:i+1] and word2[:j+1] equal
        # 1. = dp[i - 1][j - 1] if word1[i] == word2[j]
        # 2. = min(dp[i - 1][j], dp[i][j - 1]) + 1 if word1[i] != word2[j]
        n1, n2 = len(word1), len(word2)
        # pre[j] means when word1 is '', number of chars to remove to match word2[j]
        pre = [i + 1 for i in range(n2)] + [0]
        cur = [0] * (n2 + 1)
        for i in range(n1):
            # cur[-1] means when word2 is empty, need to remove i chars
            cur[-1] = i + 1
            for j in range(n2):
                cur[j] = min(cur[j - 1], pre[j]) + 1
                if word1[i] == word2[j]:
                    cur[j] = min(cur[j], pre[j - 1])
            # print(cur)
            pre, cur = cur, pre
        return pre[n2 - 1]
