###
# 给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。
# 返回 n 的长度。如果不存在这样的 n ，就返回-1。
# 注意： n 可能不符合 64 位带符号整数。
#
# 从1开始求对k的余数，直到余数为0或者出现重复的余数。
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        seen = set()
        r = 1 % k
        while r != 0 and r not in seen:
            seen.add(r)
            r = (r * 10 + 1) % k
        return len(seen) + 1 if r == 0 else -1

    def smallestRepunitDivByK1(self, k: int) -> int:
        invalid = {0, 2, 4, 5, 6, 8}
        if k % 10 in invalid:
            return -1
        r = 1 % k
        ln = 1
        cnt = set({r})
        while True:
            if r == 0:
                return ln
            # n1 means '1', n2 means '11', then n2 = n1 * 10 + 1
            # r1 = n1 % k, then r2 = (r1 * 10 + 1) % k
            r = (r * 10 + 1) % k
            ln += 1
            if r in cnt:
                return -1
            cnt.add(r)
        return -1
