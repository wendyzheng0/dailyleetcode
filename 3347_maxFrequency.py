from typing import List
from collections import defaultdict


# 给你一个整数数组 nums 和两个整数 k 和 numOperations 。
# 你必须对 nums 执行 操作  numOperations 次。每次操作中，你可以：
# 选择一个下标 i ，它在之前的操作中 没有 被选择过。
# 将 nums[i] 增加范围 [-k, k] 中的一个整数。
# 在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。
# 一个元素 x 的 频率 指的是它在数组中出现的次数。
#
# 这题和3346是一样的，昨天用了3指针的方法，今天试试差分的方法。
# 简单的说就是遍历每一个数字，每个数字可以为[num-k, num+k]中的数投票，票数最高的就是结果。
# 这个方法比3指针的方法慢。
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for num in nums:
            diff[num - k] += 1
            diff[num + k + 1] -= 1
            cnt[num] += 1
        vals = []
        pre = 0
        for c in sorted(list(diff.keys())):
            pre += diff[c]
            vals.append((pre, c))
        maxpos = max(vals)
        # print(diff)
        # print(vals)
        res = min(maxpos[0], numOperations)
        idx = 0
        for num in sorted(cnt.keys()):
            while vals[idx + 1][1] <= num:
                idx += 1
            maxoccur = min(numOperations + cnt[num], vals[idx][0])
            res = max(maxoccur, res)
        return res
