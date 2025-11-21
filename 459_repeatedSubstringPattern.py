###
# 给定一个非空的字符串 s ，检查是否可以通过由它的一个子串重复多次构成。
#
# 一开始用暴力法做的repeatedSubstringPattern1，提交能过，但是慢了点。后来看到别人用s in (s + s)[1:-1]的
# 方法，代码简洁了很多。
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern1(self, s: str) -> bool:
        p1 = 0
        p2 = s.find(s[0], 1)
        if p2 < 0:
            return False
        l = p2 - p1
        while p2 < len(s):
            if s[p1] == s[p2]:
                p1 += 1
                p2 += 1
            else:
                # print(f"p1:{p1}, p2:{p2}")
                p1 = 0
                p2 = s.find(s[0], l + 1)
                if p2 < 0:
                    return False
                l = p2 - p1
                # print(f"updated: p1:{p1}, p2:{p2}")
        return p1 % l == 0
