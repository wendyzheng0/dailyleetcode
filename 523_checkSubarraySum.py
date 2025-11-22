from typing import List


###
# 给你一个整数数组 nums 和一个整数 k ，如果 nums 有一个 好的子数组 返回 true ，否则返回 false：
# 一个 好的子数组 是：
# 长度 至少为 2 ，且
# 子数组元素总和为 k 的倍数。
# 注意：
# 子数组 是数组中 连续 的部分。
# 如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。0 始终 视为 k 的一个倍数。
#
# 任意两个位置[i,j]之间元素的和可以通过两个前缀和的差presum[j+1]-presum[i]来计算。
# 所以如果某两个元素之间的和是k的倍数，那么对应的两个前缀和对k的余数是相同的。
# 只需要记住前缀和对k的余数而不需要所有前缀和。
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # s[i+1] sum of nums[,i], then sum of [i,j] is s[j+1]-s[i-1+1], 0<=i<j<n
        # s[j+1]-s[i] = n*k, s[j+1] %k = s[i] % k
        presum = 0
        tmp = 0
        remainders = set()
        for num in nums:
            presum = (presum + num) % k
            if presum in remainders:
                return True
            remainders.add(tmp)
            tmp = presum
        return False

    def checkSubarraySum1(self, nums: List[int], k: int) -> bool:
        s = [0] * (len(nums) + 1)
        remainder = dict()
        remainder[0] = -1
        for idx, v in enumerate(nums):
            s[idx + 1] = s[idx] + v
            r = s[idx + 1] % k
            if r in remainder:
                if idx - remainder[r] >= 2:
                    return True
            else:
                remainder[r] = idx
        return False
