from typing import List
from bisect import bisect_left, bisect_right


###
# 给你一个整数数组 nums 和两个整数 k 和 numOperations 。
# 你必须对 nums 执行 操作  numOperations 次。每次操作中，你可以：
# 选择一个下标 i ，它在之前的操作中 没有 被选择过。
# 将 nums[i] 增加范围 [-k, k] 中的一个整数。
# 在执行完所有操作以后，请你返回 nums 中出现 频率最高 元素的出现次数。
# 一个元素 x 的 频率 指的是它在数组中出现的次数。
#
# 列举每个数字作为最终频率最高数字的情况，取最大值。发现没法处理当这个最大频率的数字不在nums的情况，于是增加一个循环列举
# 每个数字作为区间最小值（最终频率最高的数字-k）的情况。
###
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        uniq = set(nums)
        nums.sort()
        res = 0
        # when center is in nums, iterate every center (n)
        for n in uniq:
            nleft = bisect_left(nums, n)
            nright = bisect_right(nums, n)
            left = bisect_left(nums, n - k)
            right = bisect_right(nums, n + k)
            newoccurs = (nleft - left) + (right - nright)
            newoccurs = min(newoccurs, numOperations)
            res = max(res, nright - nleft + newoccurs)
            # print(f"n:{n}, left:{left}, nleft:{nleft}, nright:{nright}, right:{right}, maxoccurs:{nright - nleft + newoccurs}")

        # when center is not in nums, iterate every smallest bound
        # and check how many numbers occurs in [smallest, smallest + 2k]
        # the total occurances won't exceed numOperations, since all numbers
        # needs to change to get the same.
        if res >= numOperations:
            return res
        for smallest in uniq:
            nleft = bisect_left(nums, smallest)
            nright = bisect_right(nums, smallest)
            right = bisect_right(nums, smallest + k * 2)
            maxoccurs = right - nleft
            maxoccurs = min(maxoccurs, numOperations)
            res = max(res, maxoccurs)
            # print(f"smallest:{smallest}, nleft:{nleft}, nright:{nright}, right:{right}, maxoccurs:{maxoccurs}")
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxFrequency([1, 4, 5], 1, 2))  # 2
    print(s.maxFrequency([5, 11, 20, 20], 5, 1))  # 2
    print(s.maxFrequency([1, 8, 8, 8, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5, 1))  # 5
    print(s.maxFrequency([88, 53], 27, 2))  # 2
    print(s.maxFrequency([1, 90], 76, 1))  # 1
    print(s.maxFrequency([1, 5, 6, 2, 8], 10, 3))  # 4