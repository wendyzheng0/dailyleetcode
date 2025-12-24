###
# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
# 回文字符串 是正着读和倒过来读一样的字符串。
# 子字符串 是字符串中的由连续字符组成的一个序列。
#
# 遍历字符串，记录以当前字符结尾的回文字符串长度，遍历新字符的时候利用上一个字符的记录更新当前字符的记录。
class Solution:
    def countSubstrings(self, s: str) -> int:
        substrlen = [0, 1]
        res = 0
        for i, c in enumerate(s):
            newlen = [0, 1]
            # single char is palindromic substring itself
            res += 1
            for sublen in substrlen:
                pre = i - sublen - 1
                if pre >= 0 and s[pre] == c:
                    newlen.append(sublen + 2)
                    res += 1
            substrlen = newlen
        return res
