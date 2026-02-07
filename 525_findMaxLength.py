from typing import List


###
# 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。
#
# 把0变成-1，那么问题就变成寻找最长和为0的子串。遍历数组计算前缀和，相同两个前缀和之间的子串就是和为0的子串
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pos = {0: -1}
        s = 0
        res = 0
        for idx, v in enumerate(nums):
            s += 1 if v else -1
            if s in pos:
                res = max(res, idx - pos[s])
            else:
                pos[s] = idx
        return res
