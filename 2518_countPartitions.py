from typing import List


###
# 给你一个正整数数组 nums 和一个整数 k 。
# 分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。
# 返回 不同 的好分区的数目。由于答案可能很大，请返回对 10^9 + 7 取余 后的结果。
# 如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。
#
# f[i]表示前x个元素中，和为i的子集个数。
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        if s < k * 2:
            return 0
        MOD = 1_000_000_007
        f = [0] * k
        f[0] = 1
        for num in nums:
            for c in range(k - 1, num - 1, -1):
                f[c] = (f[c] + f[c - num]) % MOD
        # print(f)
        return ((1 << len(nums)) % MOD - sum(f) * 2) % MOD
