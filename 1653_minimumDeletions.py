###
# 给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。
# 你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。
# 请你返回使 s 平衡 的 最少 删除次数。
#
# minimumDeletions1是分别记录字串s[:i+1]需要删除几个字符串可以获得结尾为‘a'或’b'的子串。最后统计谁删的少。
# 后来看了官方解答得到minimumDeletions，先构造只包含a的子串，然后转变过程中检查最少删除字符数。
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # turn s to only contains 'b'
        res = delete = s.count('a')
        # turn s to only contains 'a' and check chars deleted during the process
        for c in s:
            if c == 'a':
                delete -= 1
            else:
                delete += 1
            if res > delete:
                res = delete
        return res

    def minimumDeletions1(self, s: str) -> int:
        idx = s.find('b')
        enda, endb = 0, 0
        while idx < len(s):
            if s[idx] == 'a':
                endb = endb + 1
            else:
                endb = min(enda, endb)
                enda = enda + 1
            idx += 1
        return min(enda, endb)
