from collections import Counter


###
# 给你两个长度均为 n 且仅由小写英文字母组成的字符串 s 和 target。
# 返回 s 的 字典序最小的排列，要求该排列 严格 大于 target。如果 s 不存在任何字典序严格大于 target 的排列，则返回一个空字符串。
# 如果两个长度相同的字符串 a 和 b 在它们首次出现不同字符的位置上，字符串 a 对应的字母在字母表中出现在 b 对应字母的 后面 ，则字符串 a 字典序严格大于 字符串 b。
# 排列 是字符串中所有字符的一种重新排列。
#
# 先用s的字符构造和target最长公共前缀字符串，直到s中没有足够的字符为止。然后从后往前遍历target，尝试把第idx位改成s中比target[idx]大的最小字符，如果存在再由s剩下的字符继续构造剩下的部分。
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        for idx, c in enumerate(target):
            if c in cnt and cnt[c] > 0:
                cnt[c] -= 1
            else:
                break
        else:
            cnt[target[idx]] += 1
        while idx >= 0:
            for c in sorted(list(cnt.keys())):
                if target[idx] < c and cnt[c] > 0:
                    break
            else:
                idx -= 1
                cnt[target[idx]] += 1
                continue
            # print(f"use {c} replace target[{idx}]")
            res = target[:idx]
            res += c
            cnt[c] -= 1
            res += ''.join(c * cnt[c] for c in sorted(cnt.keys()) if cnt[c] > 0)
            # print(res)
            return res
        return ''
