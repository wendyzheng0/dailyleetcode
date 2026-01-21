from typing import List


###
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
#
# 开始还先算每两个数的和然后两两配对，结果超时了。最后改成这种逐个遍历的方法再加上优化。
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            if nums[a] + sum(nums[-3:]) < target:
                continue
            if sum(nums[a:a + 4]) > target:
                break
            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                if nums[a] + nums[b] + sum(nums[-2:]) < target:
                    continue
                if nums[a] + sum(nums[b:b + 3]) > target:
                    break
                sub = target - nums[a] - nums[b]
                left, right = b + 1, n - 1
                while left < right:
                    if nums[left] + nums[right] > sub:
                        right -= 1
                    elif nums[left] + nums[right] < sub:
                        left += 1
                    else:
                        res.add((nums[a], nums[b], nums[left], nums[right]))
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return list(list(v) for v in res)
