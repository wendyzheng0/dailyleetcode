from typing import List


###
# 给你一个整数数组 nums 和一个 正整数 k 。
# 请你统计有多少满足 「 nums 中的 最大 元素」至少出现 k 次的子数组，并返回满足这一条件的子数组的数目。
# 子数组是数组中的一个连续元素序列。
#
# 滑动窗口。左端点不动，找合法右端点。找到一个之后左端点边右移边收集合法子数组，直到变成不合法，再继续移动右端点。
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxval = max(nums)
        maxcnt = 0
        left, right = 0, 0
        res = 0
        while left <= right < n:
            if right < n and nums[right] == maxval:
                maxcnt += 1
            while left <= right and maxcnt >= k:
                res += n - right
                if nums[left] == maxval:
                    maxcnt -= 1
                left += 1
            right += 1

        return res
