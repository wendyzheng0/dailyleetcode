from typing import List
from math import inf
from itertools import pairwise


###
# 给你个整数数组 arr，其中每个元素都 不相同。
# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。
# 每对元素对 [a,b] 如下：
# a , b 均为数组 arr 中的元素
# a < b
# b - a 等于 arr 中任意两个元素的最小绝对差
#
# 先排序，然后遍历一遍，记录最小绝对差和对应的元素对。
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = inf
        minarr = []
        for x, y in pairwise(arr):
            if y - x < mindiff:
                mindiff = y - x
                minarr = [[x, y]]
            elif y - x == mindiff:
                minarr.append([x, y])
        return minarr
