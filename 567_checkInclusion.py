from collections import Counter, defaultdict


###
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
# 先计算s1各个字符出现次数，再扫描s2，记录起始位置，统计各个字符出现次数。如果发现不存在的字符，重新开始计算。如果某个字符超了
# 从起始位置开始回退直到不超为止。如果匹配长度等于s1长度，则返回True。
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len2 < len1:
            return False
        cnt1 = Counter(s1)
        cnt2 = defaultdict(int)
        matchlen = 0
        start = 0
        for i, c in enumerate(s2):
            if c not in cnt1:
                cnt2 = defaultdict(int)
                matchlen = 0
                start = i + 1
            else:
                cnt2[c] += 1
                matchlen += 1
                while cnt2[c] > cnt1[c]:
                    cnt2[s2[start]] -= 1
                    matchlen -= 1
                    start += 1
                if matchlen == len1:
                    return True
        return False
