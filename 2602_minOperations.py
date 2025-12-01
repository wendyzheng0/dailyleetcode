from typing import List
from bisect import bisect_left


###
# 给你一个正整数数组 nums 。
# 同时给你一个长度为 m 的整数数组 queries 。第 i 个查询中，你需要将 nums 中所有元素变成 queries[i] 。你可以执行以下操作 任意 次：
# 将数组里一个元素 增大 或者 减小 1 。
# 请你返回一个长度为 m 的数组 answer ，其中 answer[i]是将 nums 中所有元素变成 queries[i] 的 最少 操作次数。
# 注意，每次查询后，数组变回最开始的值。
#
# 数组的和可以认为是把nums所有元素变成0所需要的操作数。那么把所有元素变成q所需要的操作数就分两部分：
# 1. 小于q的元素变成q所需要的操作数。为q - x
# 2. 大于q的元素变成q所需要的操作数。为x - q
# 把nums排序再利用前缀和就可以快速的计算小于q的元素的和与大于q的元素的和，进而得到他们变成q所需要的操作总数。
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        # presum = list(accumulate(nums, initial=0))
        res = []
        for q in queries:
            p = bisect_left(nums, q)
            s1 = p * q - presum[p]
            s2 = (presum[n] - presum[p]) - (n - p) * q
            res.append(s1 + s2)
        return res
