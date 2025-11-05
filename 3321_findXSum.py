from typing import List
from collections import Counter
from sortedcontainers import SortedList


###
# 给你一个由 n 个整数组成的数组 nums，以及两个整数 k 和 x。
# 数组的 x-sum 计算按照以下步骤进行：
# 统计数组中所有元素的出现次数。
# 仅保留出现次数最多的前 x 个元素的每次出现。如果两个元素的出现次数相同，则数值 较大 的元素被认为出现次数更多。
# 计算结果数组的和。
# 注意，如果数组中的不同元素少于 x 个，则其 x-sum 是数组的元素总和。
# 返回一个长度为 n - k + 1 的整数数组 answer，其中 answer[i] 是 子数组 nums[i..i + k - 1] 的 x-sum。
# 子数组 是数组内的一个连续 非空 的元素序列。
#
# 跟3318_findXSum.py一样的描述，但是取值范围大了几个数量级。原来的方法完全没用了。利用一点点更新的方法，并用了
# 两个SortedList来缓存出现次数最多的前x个元素和剩余元素。每次更新都需要维护这两个SortedList。
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        topx = SortedList()
        remainders = SortedList()
        res = []
        cnt = Counter(nums[:k - 1])
        topx = SortedList([c, n] for n, c in cnt.items())
        topxsum = sum(c * n for n, c in cnt.items())
        for idx, num in enumerate(nums[k - 1:]):
            if cnt[num] > 0:
                p = [cnt[num], num]
                if p in topx:
                    topx.remove(p)
                    topxsum -= p[0] * p[1]
                else:
                    remainders.remove(p)
            cnt[num] += 1
            p = [cnt[num], num]
            if topx and p > topx[0]:
                topx.add(p)
                topxsum += p[0] * p[1]
            else:
                remainders.add(p)
            while len(topx) > x:
                p = topx[0]
                topxsum -= p[0] * p[1]
                remainders.add(p)
                topx.pop(0)
            while remainders and len(topx) < x:
                p = remainders[-1]
                topxsum += p[0] * p[1]
                topx.add(p)
                remainders.pop(-1)
            res.append(topxsum)
            first = nums[idx]
            p = [cnt[first], first]
            if p in topx:
                topx.remove(p)
                topxsum -= p[0] * p[1]
            else:
                remainders.remove(p)
            cnt[first] -= 1
            if cnt[first] > 0:
                p = [cnt[first], first]
                if topx and p > topx[0]:
                    topx.add(p)
                    topxsum += p[0] * p[1]
                else:
                    remainders.add(p)
        return res
