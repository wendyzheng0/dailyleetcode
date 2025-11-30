from typing import List
from math import inf


###
# 给你一个整数数组 nums。
# 镜像对 是指一对满足下述条件的下标 (i, j)：
# 0 <= i < j < nums.length，并且
# reverse(nums[i]) == nums[j]，其中 reverse(x) 表示将整数 x 的数字反转后形成的整数。反转后会忽略前导零，例如 reverse(120) = 21。
# 返回任意镜像对的下标之间的 最小绝对距离。下标 i 和 j 之间的绝对距离为 abs(i - j)。
# 如果不存在镜像对，返回 -1。
#
# 用dict记录之前出现过的镜像对，边遍历nums边检查有没有出现过，然后更新res
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        reverse = dict()
        res = inf
        for j, v in enumerate(nums):
            if v in reverse:
                res = min(res, j - reverse[v])
            r = 0
            while v > 0:
                r = r * 10 + v % 10
                v = v // 10
            reverse[r] = j
        return res if res < inf else -1
