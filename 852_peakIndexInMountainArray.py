from typing import List


###
# 给定一个长度为 n 的整数 山脉 数组 arr ，其中的值递增到一个 峰值元素 然后递减。
# 返回峰值元素的下标。
# 你必须设计并实现时间复杂度为 O(log(n)) 的解决方案。
#
# 二分查找
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid
            # print(f"{left}, {right}")
        return left
