###
# 3003. 执行操作后的最大分割数量
# 给你一个下标从 0 开始的字符串 s 和一个整数 k。
# 你需要执行以下分割操作，直到字符串 s 变为 空：
# * 选择 s 的最长 前缀，该前缀最多包含 k 个 不同 字符。
# * 删除 这个前缀，并将分割数量加一。如果有剩余字符，它们在 s 中保持原来的顺序。
# 执行操作之 前 ，你可以将 s 中 至多一处 下标的对应字符更改为另一个小写英文字母。
# 在最优选择情形下改变至多一处下标对应字符后，用整数表示并返回操作结束时得到的 最大 分割数量。
#
# 这题比较难，学习了灵神的题解写出来的。
# 灵神的题解：https://leetcode.cn/problems/maximize-the-number-of-partitions-after-operations/solutions/2595072/ji-yi-hua-sou-suo-jian-ji-xie-fa-pythonj-6g5z/?envType=daily-question&envId=2025-10-17
# 修改最多只能改一次。当一个字符串确定之后，有多少分割数也是确定的，于是只需要历遍每一个位置，
# 看每个位置修改后的分割数量。根据重要的定理，从左边分和从右边开始分得到的数量是一样的，具体证明看
# 题解。于是就可以不用每次历遍一个位置的时候都算一次右边可以分为几段了。

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1
        n = len(s)
        charset = set()
        sufMask = [set() for _ in range(n + 1)]
        sufSeg = [1 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            if s[i] in charset:
                sufMask[i] = sufMask[i + 1]
                sufSeg[i] = sufSeg[i + 1]
                continue
            if len(charset) == k:
                sufSeg[i] = sufSeg[i + 1] + 1
                charset = set({s[i]})
            else:
                sufSeg[i] = sufSeg[i + 1]
                charset.add(s[i])
            sufMask[i] = charset.copy()
        # print(sufMask)
        # print(sufSeg)

        charset = set()
        preMask = set()
        preSeg = 1
        res = 0
        for i in range(n):
            # print(f"i: {i}, preSeg:{preSeg}, preMask:{preMask}")
            uniSize = len(preMask.union(sufMask[i + 1]))
            if uniSize < k:
                segs = sufSeg[i + 1] + preSeg - 1
            elif uniSize < 26 and len(preMask) == k and len(sufMask[i + 1]) == k:
                segs = sufSeg[i + 1] + preSeg + 1
            else:
                segs = sufSeg[i + 1] + preSeg
            # print(f"segs: {segs}")
            res = max(res, segs)
            if len(preMask) == k and s[i] not in preMask:
                preSeg += 1
                preMask = set({s[i]})
            else:
                preMask.add(s[i])

        return res
