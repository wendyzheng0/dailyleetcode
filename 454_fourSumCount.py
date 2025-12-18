from typing import List
from collections import Counter


###
# 给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
# 开始的时候先排序然后尝试写3层循环，结果超时。后来改成分别统计nums1和nums2可能的和以及nums3和nums4可能的和，然后检查是否存在相反数。
# 借助Counter写了个很python的解法
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = Counter([v1 + v2 for v1 in nums1 for v2 in nums2])
        return sum(cnt[-v3 - v4] for v3 in nums3 for v4 in nums4)
