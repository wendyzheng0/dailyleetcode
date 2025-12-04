from typing import List
from bisect import bisect_right, bisect_left


###
# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 请你找出符合题意的 最短 子数组，并输出它的长度。
#
# 先找出最左边需要排序的位置，如果不存在，直接返回0.然后找出最右边需要排序的位置。对于中间的子数组，还需要找出其中
# 的最大值最小值，然后调整左右边界。
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = n, -1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                left = i - 1
                break
        if left == n:
            return 0
        for i in range(n - 2, left - 1, -1):
            if nums[i] > nums[i + 1]:
                right = i + 1
                break
        t = nums[left:right + 1]
        left = bisect_right(nums[:left], min(t))
        right = bisect_left(nums[right + 1:], max(t)) + right
        # print(f"left:{left}, right:{right}")
        return right - left + 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findUnsortedSubarray([2,6,4,8,10,9,15])) # 5
    print(solution.findUnsortedSubarray([1,2,3,4])) # 0
    print(solution.findUnsortedSubarray([1])) # 0
    print(solution.findUnsortedSubarray([1,3,2,2,2]))  # 4
    print(solution.findUnsortedSubarray([1,2,4,5,3]))  # 3
    print(solution.findUnsortedSubarray([1,2,4,2,5,3,5,6]))  # 4