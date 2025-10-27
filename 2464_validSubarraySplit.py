from typing import List
from math import inf
from functools import cache
from math import gcd


###
# 给定一个整数数组 nums。
# 如果要将整数数组 nums 拆分为 子数组 后是 有效的，则必须满足:
# 每个子数组的第一个和最后一个元素的最大公约数 大于 1，且
# nums 的每个元素只属于一个子数组。
# 返回 nums 的 有效 子数组拆分中的 最少 子数组数目。如果不能进行有效的子数组拆分，则返回 -1。
# 注意:
# 两个数的 最大公约数 是能整除两个数的最大正整数。
# 子数组 是数组中连续的非空部分。
#
# 动态规划（validSubarraySplit）：f[i]表示前i个元素的子数组拆分最少数量
# 记忆化搜索（validSubarraySplit1）：dfs(i, j)表示从i到j的子数组拆分最少数量，速度略快
class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        f = [inf] * (len(nums) + 1)
        f[-1] = 0
        f[0] = 1 if nums[0] > 1 else 0
        for i in range(len(nums)):
            for j in range(i + 1):
                if gcd(nums[j], nums[i]) > 1:
                    f[i] = min(f[i], f[j - 1] + 1)
            # print(f"i: {i}, f:{f}")
        return f[-2] if f[-2] != inf else -1

    def validSubarraySplit1(self, nums: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 1 if nums[i] > 1 else -1
            res = inf
            for k in range(j - 1, i - 1, -1):
                if gcd(nums[i], nums[k]) > 1:
                    if k + 1 == j:
                        res = 1
                        break
                    ret = dfs(k + 1, j)
                    if ret > 0:
                        res = min(res, ret + 1)
            # print(f"i:{i}, j:{j}, res:{res}")
            return res if res != inf else -1
        return dfs(0, len(nums))
