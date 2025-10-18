
from typing import List


###
# 给你一个整数数组 nums 和一个整数 k。
# 你可以对数组中的每个元素 最多 执行 一次 以下操作：
# 将一个在范围 [-k, k] 内的整数加到该元素上。
# 返回执行这些操作后，nums 中可能拥有的不同元素的 最大 数量。
#
# 贪心算法，先把数组排序，然后从最小的数开始尝试分配可用的最小值 minavail，
# 如果一个数无法分配，则跳过它，继续尝试下一个数。
###
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        minavail = nums[0] - k
        for num in nums:
            if abs(minavail - num) <= k:
                res += 1
                minavail += 1
            elif num - k > minavail:
                res += 1
                minavail = num - k + 1
        return res
