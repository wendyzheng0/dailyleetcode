from typing import List
from math import inf


###
# 给你一个 下标从 0 开始 的整数数组 nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。
# 从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分 和 最低分 的 差值 达到 最小化 。
# 返回可能的 最小差值 。
#
# 排序后遍历一次即可找到最小差值
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = inf
        for i in range(k - 1, len(nums)):
            res = min(res, nums[i] - nums[i - k + 1])
        return res
