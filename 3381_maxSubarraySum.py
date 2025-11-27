from typing import List


###
# 给你一个整数数组 nums 和一个整数 k 。
# 返回 nums 中一个 非空子数组 的 最大 和，要求该子数组的长度可以 被 k 整除。
#
# 开始的时候尝试用dp，先算出第j个元素结尾的长为k的子串和，然后计算长为k的其他倍数i时和的最大值。
# dp[i,j] = dp[i-1,j] + dp[1, j-(i-1)*k], 这个解法超时了。
# 观察上面的式子发现dp[i,j]最后是由若干个dp[1,x]组成的，而且x间隔是k，可以用滑动窗口的方法求解。
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ksum = [sum(nums[:k])]
        for i in range(k, n):
            ksum.append(ksum[-1] + nums[i] - nums[i - k])
        res = max(ksum)
        for i in range(k):
            x = ksum[i:n:k]
            p = 0
            for v in x:
                p = max(p + v, v)
                res = max(res, p)

        return res
