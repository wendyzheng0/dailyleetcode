from typing import List


###
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 pivot 。请你将 nums 重新排列，使得以下条件均成立：
# 所有小于 pivot 的元素都出现在所有大于 pivot 的元素 之前 。
# 所有等于 pivot 的元素都出现在小于和大于 pivot 的元素 中间 。
# 小于 pivot 的元素之间和大于 pivot 的元素之间的 相对顺序 不发生改变。
# 更正式的，考虑每一对 pi，pj ，pi 是初始时位置 i 元素的新位置，pj 是初始时位置 j 元素的新位置。如果 i < j 且两个元素 都 小于（或大于）pivot，那么 pi < pj 。
# 请你返回重新排列 nums 数组后的结果数组。
#
# 这题比较直观，直接遍历一遍，把小于pivot的元素放到smaller，等于pivot的元素放到equal，大于pivot的元素放到larger，然后合并。
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = 0
        larger = []
        for v in nums:
            if v < pivot:
                smaller.append(v)
            elif v == pivot:
                equal += 1
            else:
                larger.append(v)
        return smaller + [pivot] * equal + larger
