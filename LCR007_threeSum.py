from typing import List


###
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。
#
# 排序后，固定第一个数，然后使用双指针法找到另外两个数。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        va = 100001
        for a in range(n - 2):
            if nums[a] == va:
                continue
            va = nums[a]
            b = a + 1
            c = n - 1
            while b < c:
                # print(f"{nums[b]}, {nums[c]}")
                s = nums[b] + nums[c]
                if s > -va:
                    c -= 1
                elif s < -va:
                    b += 1
                else:
                    vb = nums[b]
                    vc = nums[c]
                    res.append([va, vb, vc])
                    while b < c and nums[b] == vb:
                        b += 1
                    while b < c and nums[c] == vc:
                        c -= 1
        return res
