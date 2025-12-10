from typing import List


###
# 给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。
#
# 因为要找最大运算结果，从结果可能的最高位开始尝试填1，如果填1后能找到两个数，使得它们的异或结果在那一位为1，那就填1，否则填0。
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        high = max(nums).bit_length() - 1
        res = 0
        for i in range(high, -1, -1):
            mask = 1 << i | res
            seen = set()
            for v in nums:
                prefix = v >> i << i
                if mask ^ prefix in seen:
                    res = mask
                    break
                seen.add(prefix)
        return res
