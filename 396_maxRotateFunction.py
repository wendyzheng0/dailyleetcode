from typing import List


###
# 给定一个长度为 n 的整数数组 nums 。
# 假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
# 返回 F(0), F(1), ..., F(n-1)中的最大值 。
# 生成的测试用例让答案符合 32 位 整数。
#
# 观察F函数的规律就发现F(i)=F(i-1)+sum(nums)-n*nums[n-i]，所以只需要计算F(0)和sum(nums)，
# 然后遍历一遍计算F(i)，取最大值。
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # f[i] = 0 * nums[i] + 1 * nums[i + 1] + ... + (n - 1) * nums[n - i - 1]
        # f[i + 1] = 0 * nums[i - 1] + 1 * nums[i] + ... + (n - 1) * nums[n - i - 2]
        # = f[i] + sum(nums) - nums[n - i - 1] - (n - 1) * nums[n - i - 1]
        # = f[i] + sum(nums) - n * nums[n - i - 1]
        n = len(nums)
        res = pre = sum(i * v for i, v in enumerate(nums))
        arrsum = sum(nums)
        for i in range(1, n):
            pre = pre + arrsum - n * nums[n - i]
            res = max(res, pre)
        return res
