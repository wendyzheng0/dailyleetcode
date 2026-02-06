from typing import Counter, List
from bisect import bisect_left
from math import inf


###
# 给你一个整数数组 nums 和一个整数 k。
# 如果一个数组的 最大 元素的值 至多 是其 最小 元素的 k 倍，则该数组被称为是 平衡 的。
# 你可以从 nums 中移除 任意 数量的元素，但不能使其变为 空 数组。
# 返回为了使剩余数组平衡，需要移除的元素的 最小 数量。
# 注意：大小为 1 的数组被认为是平衡的，因为其最大值和最小值相等，且条件总是成立。
#
# 用滑动窗口求解。
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        numcnt = list(Counter(nums).items())
        numcnt.sort()
        # print(numcnt)
        startpos = endpos = 0
        left, right = 0, sum(v for _, v in numcnt)
        res = inf
        while endpos < len(numcnt):
            end = numcnt[startpos][0] * k + 1
            newendpos = bisect_left(numcnt, (end, 0), endpos)
            right -= sum(v for _, v in numcnt[endpos:newendpos])
            if left + right < res:
                res = left + right
                if res == 0:
                    return res
            left += numcnt[startpos][1]
            startpos += 1
            endpos = newendpos
        return res
