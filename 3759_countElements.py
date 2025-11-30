from typing import List
from bisect import bisect_left


###
# 给你一个长度为 n 的整数数组 nums 和一个整数 k。
# 如果数组 nums 中的某个元素满足以下条件，则称其为 合格元素：存在 至少 k 个元素 严格大于 它。
# 返回一个整数，表示数组 nums 中合格元素的总数。
#
# 利用python的函数快速排序和查找第k大元素的位置，从而得到有多少个数比第k大的数要小。
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        return bisect_left(nums, nums[-k]) if k > 0 else len(nums)
