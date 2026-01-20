from typing import List


###
# 给你一个长度为 n 的质数数组 nums 。你的任务是返回一个长度为 n 的数组 ans ，对于每个下标 i ，以下 条件 均成立：
# ans[i] OR (ans[i] + 1) == nums[i]
# 除此以外，你需要 最小化 结果数组里每一个 ans[i] 。
# 如果没法找到符合 条件 的 ans[i] ，那么 ans[i] = -1 。
# 质数 指的是一个大于 1 的自然数，且它只有 1 和自己两个因数。
#
# 对于每个数，找到右边第一个0，把这个0右边的第一个1变成0，其他位保持不变。
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            right = 0
            n = 0
            while num & 1 == 1:
                num = num >> 1
                if num & 1 == 1:
                    right = (right << 1) | 1
                n += 1
            if n == 0:
                res.append(-1)
            else:
                # print(f"num:{num}, n:{n}, right:{right}")
                res.append(num << n | right)
        return res
