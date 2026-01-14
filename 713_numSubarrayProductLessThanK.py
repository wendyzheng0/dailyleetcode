from typing import List


###
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
#
# 由于是连续子数组，所以用滑动窗口比较适合。保持当前字符结束的满足条件的窗口，随着遍历计算新增的满足条件的子数组数量。
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        # start idx of cur subarray
        s = 0
        prod = 1
        res = 0
        for i in range(len(nums)):
            prod *= nums[i]
            while s <= i and prod >= k:
                prod = prod // nums[s]
                s += 1
            res += i - s + 1
        return res
