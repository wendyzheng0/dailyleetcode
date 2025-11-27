###
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长连续子字符串 的长度。
#
# 一边遍历字符串一边记录出现过的字符的序号，一旦出现重复字符，则从上一个重复字符的下一个位置开始重新计算。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chset = dict()
        start = 0
        res = 0
        for idx, c in enumerate(s):
            if c not in chset or chset[c] < start:
                chset[c] = idx
            else:
                res = max(res, idx - start)
                start = chset[c] + 1
                chset[c] = idx
        res = max(res, len(s) - start)
        return res
