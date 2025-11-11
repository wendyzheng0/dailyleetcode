from typing import List


###
# 给定一个长度为 n 的整数数组和一个目标值 target ，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。
#
# 先排序，然后遍历第一个数nums[i]，再用双指针找第二nums[j]第三个数nums[k]，利用单调性，找到一对之后，第三个数就可以取到k-j个。
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            k = n - 1
            subtarget = target - nums[i]
            for j in range(i + 1, n - 1):
                while nums[j] + nums[k] >= subtarget and j < k:
                    k -= 1
                if j >= k:
                    break
                res += k - j
                # print(f"i:{i}, j:{j}, k:{k} res:{res}")
        return res
