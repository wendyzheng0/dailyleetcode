from typing import List


###
# 给你一个长度为 n 的整数数组 nums 。
# 分区 是指将数组按照下标 i （0 <= i < n - 1）划分成两个 非空 子数组，其中：
# 左子数组包含区间 [0, i] 内的所有下标。
# 右子数组包含区间 [i + 1, n - 1] 内的所有下标。
# 对左子数组和右子数组先求元素 和 再做 差 ，统计并返回差值为 偶数 的 分区 方案数。
#
# 只有和为偶数时有解，且任意分割都满足，解为n-1。
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return 0 if sum(nums) % 2 == 1 else len(nums) - 1
