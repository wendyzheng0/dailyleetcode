from typing import List
from math import inf


###
# 给你一个下标从 0 开始的数组 nums 和一个整数 target 。
# 下标从 0 开始的数组 infinite_nums 是通过无限地将 nums 的元素追加到自己之后生成的。
# 请你从 infinite_nums 中找出满足 元素和 等于 target 的 最短 子数组，并返回该子数组的长度。如果不存在满足条件的子数组，返回 -1 。
#
# 由于子数组是连续的，所以可以用滑动窗口求解。
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        res = (target // s) * n
        subtarget = target % s
        if subtarget == 0:
            return res
        csum = 0
        start = 0
        subres = inf
        for i in range(2 * n):
            csum += nums[i % n]
            while csum > subtarget:
                csum -= nums[start % n]
                start += 1
            if csum == subtarget:
                subres = min(subres, i - start + 1)
        return res + subres if subres != inf else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSizeSubarray([1, 2, 3], 5))  # 2
    print(solution.minSizeSubarray([1,1,1,2,3], 4))  # 2
    print(solution.minSizeSubarray([2,4,6,8], 3))  # -1
    print(solution.minSizeSubarray([2,4,6,8,1], 23))  # 6
    print(solution.minSizeSubarray([1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6], 56))  # 16