from typing import List
from collections import Counter


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
# findXSum1是自己想的方法，想着用一个数组记录各个数字出现的次数，然后每次计算都更新一下。结果发现还没有每次利用
# python的Counter都算一次的速度快.估计是数据量比较少的原因。
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        n = len(nums)
        if x >= k:
            for i in range(n - k + 1):
                res.append(sum(nums[i:i + k]))
        else:
            for i in range(n - k + 1):
                if len(set(nums[i: i + k])) <= x:
                    res.append(sum(nums[i:i + k]))
                else:
                    res.append(sum(v * k for v, k in sorted([[v, k] for k, v in Counter(nums[i: i + k]).items()], reverse=True)[:x]))
        return res

    def findXSum1(self, nums: List[int], k: int, x: int) -> List[int]:
        occurs = [[0, i] for i in range(51)]
        for i in range(k):
            occurs[nums[i]][0] += 1
        res = []
        n = len(nums)
        for i in range(n - k + 1):
            sortedocc = sorted(occurs, reverse=True)
            # print(sortedocc[:x])
            r = 0
            for j in range(x):
                r += sortedocc[j][0] * sortedocc[j][1]
            res.append(r)
            if i + k >= n:
                break
            occurs[nums[i]][0] -= 1
            occurs[nums[i + k]][0] += 1
        return res
