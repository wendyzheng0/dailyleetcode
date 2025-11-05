from typing import List
from collections import defaultdict

###
# 给你一个非负整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
# 开始的时候没有想到用背包问题的方法解，直接穷举findTargetSumWays1，虽然能过但速度很慢。
# 看了灵神的解答尝试用背包问题的方法。S是nums的和，S+target就是正符号整数和的2倍，S-target就是负符号整数和的2倍。
# 所以问题就可以转化为在nums里面寻找和为(S-｜target｜)/2的子集的数目。f[i]表示前面已遍历的数里和为i的子集的数目。
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # s = 2 * sum(<less sign numbers>)
        s = sum(nums) - abs(target)
        if s < 0 or s % 2 != 0:
            return 0
        s = s // 2
        f = [1] + [0] * s
        for num in nums:
            for i in range(s, num - 1, -1):
                f[i] += f[i - num]
            # print(f)
        return f[s]

    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        value = defaultdict(int)
        value[0] = 1
        for num in nums:
            newval = defaultdict(int)
            for presum, cnt in value.items():
                v = presum + num
                newval[v] += cnt
                v = presum - num
                newval[v] += cnt
            # print(newval)
            value = newval
        return value[target]
