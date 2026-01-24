from typing import List


###
# 给你一个长度为 n 的整数数组 nums，其中 nums 是范围 [0..n - 1] 内所有数字的一个 排列 。
# 你可以在满足条件 nums[i] AND nums[j] == k 的情况下交换下标 i 和 j 的元素，其中 AND 表示按位与操作，k 是一个非负整数。
# 返回可以使数组按 非递减 顺序排序的最大值 k（允许进行任意次这样的交换）。如果 nums 已经是有序的，返回 0。
# 排列 是数组所有元素的一种重新排列。
#
# 由于只能有一个k，所有位置不对的数字都必须通过两两相交为k的数字来交换。
# 所以最大的k就是所有位置不对的数字的按位与。
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0
        res = 0
        tomove = [v for i, v in enumerate(nums) if i != v]
        # print(tomove)
        if tomove:
            res = tomove[0]
            for v in tomove:
                res &= v
        return res
