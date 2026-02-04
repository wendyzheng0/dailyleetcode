from collections import pairwise
from math import inf
from typing import List


###
# 给你一个长度为 n 的整数数组 nums。
# 三段式子数组 是一个连续子数组 nums[l...r]（满足 0 <= l < r < n），并且存在下标 l < p < q < r，使得：
# nums[l...p] 严格 递增，
# nums[p...q] 严格 递减，
# nums[q...r] 严格 递增。
# 请你从数组 nums 的所有三段式子数组中找出和最大的那个，并返回其 最大 和。
#
# 开始的时候用比较笨的办法maxSumTrionic1，把所有严格降的段都找出来，然后遍历扩展。
# 看了灵神的题解可以利用状态机的方法简单很多。f1,f2,f3分别表示当前元素做第1，2，3段最后一个元素的时候的最大和。
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        res = f1 = f2 = f3 = -inf
        for x, y in pairwise(nums):
            f3 = max(f3, f2) + y if x < y else -inf
            f2 = max(f2, f1) + y if x > y else -inf
            f1 = max(f1, x) + y if x < y else -inf
            res = max(res, f3)
        return res

    def maxSumTrionic1(self, nums: List[int]) -> int:
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        i = 1
        desc = []
        while i < len(diff):
            if diff[i] < 0:
                start = i
                while i + 1 < len(diff) and diff[i + 1] < 0:
                    i += 1
                desc.append((start, i))
            i += 1
        # print(diff)
        # print(desc)
        res = -inf
        for desc1, desc2 in desc:
            l = desc1
            while l >= 1 and diff[l - 1] > 0:
                l -= 1
                if l >= 1 and nums[l - 1] <= 0:
                    break
            if diff[l] <= 0:
                continue
            r = desc2
            while r + 1 < len(diff) and diff[r + 1] > 0:
                r += 1
            if r >= len(diff) or diff[r] <= 0:
                continue
            r += 1
            # print(f"s1: {l}, {r + 1}, s2: {l}, {desc2 + 3}")
            s = sum(nums[l:r + 1])
            s2 = sum(nums[l: desc2 + 3]) # only take one digit after desc2
            res = max(res, s, s2)
        return res
