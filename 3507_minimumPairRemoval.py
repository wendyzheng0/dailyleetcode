from typing import List
from math import inf


###
# 给你一个数组 nums，你可以执行以下操作任意次数：
# 选择 相邻 元素对中 和最小 的一对。如果存在多个这样的对，选择最左边的一个。
# 用它们的和替换这对元素。
# 返回将数组变为 非递减 所需的 最小操作次数 。
# 如果一个数组中每个元素都大于或等于它前一个元素（如果存在的话），则称该数组为非递减。
#
# 根据题意更新nums，直到nums非递减为止。
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0
        while len(nums) > 1:
            needexchange = False
            minidx = -1
            minsum = inf
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    needexchange = True
                if nums[i] + nums[i - 1] < minsum:
                    minsum = nums[i] + nums[i - 1]
                    minidx = i - 1
            if needexchange:
                del nums[minidx]
                nums[minidx] = minsum
                res += 1
            else:
                break
        return res
