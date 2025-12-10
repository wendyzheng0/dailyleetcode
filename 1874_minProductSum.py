from typing import List


###
# 给定两个长度相等的数组a和b，它们的乘积和为数组中所有的a[i] * b[i]之和，其中0 <= i < a.length。
# 比如a = [1,2,3,4]，b = [5,2,3,1]时，它们的乘积和为1*5 + 2*2 + 3*3 + 4*1 = 22
# 现有两个长度都为n的数组nums1和nums2，你可以以任意顺序排序nums1，请返回它们的最小乘积和。
#
# 把nums1排序，nums2排序后倒序，然后对应位置相乘求和。
class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)
        res = 0
        for x, y in zip(nums1, nums2):
            res += x * y
        return res
