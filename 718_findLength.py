from typing import List
from collections import defaultdict


###
# 给两个整数数组 nums1 和 nums2 ，返回 两个数组中 公共的 、长度最长的子数组的长度 。
#
# 开始的时候想着直接比较，结果虽然过了，但是速度比较慢。后来换成了最长公共子序列类似的动态规划算法，速度马上上去了。
# ps：哪怕是动态规划算法，如果res是每次更新的话依然很慢，所以需要放到最后一起算最大值。
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        f = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    f[i + 1][j + 1] = f[i][j] + 1
        return max(max(v) for v in f)

    def findLength1(self, nums1: List[int], nums2: List[int]) -> int:
        loc = defaultdict(list)
        n1, n2 = len(nums1), len(nums2)
        for i, v in enumerate(nums1):
            loc[v].append(i)
        # print(loc)
        res = 0
        for j, t in enumerate(nums2):
            if n1 - j < res:
                break
            for k in loc[t]:
                if n2 - k < res:
                    break
                p1, p2 = k, j
                cnt = 0
                while p1 < n1 and p2 < n2 and nums1[p1] == nums2[p2]:
                    p1 += 1
                    p2 += 1
                    cnt += 1
                res = max(res, cnt)
        return res
