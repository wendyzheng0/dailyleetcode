from typing import List


###
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 value 。
# 在一步操作中，你可以对 nums 中的任一元素加上或减去 value 。
# 例如，如果 nums = [1,2,3] 且 value = 2 ，你可以选择 nums[0] 减去 value ，得到 nums = [-1,2,3] 。
# 数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。
# 例如，[-1,2,3] 的 MEX 是 0 ，而 [1,0,3] 的 MEX 是 2 。
# 返回在执行上述操作 任意次 后，nums 的最大 MEX 。
#
# 这里找的是最小的非负整数，所以对每个数取模 value 后，统计每个余数出现的次数。
# 出现次数最少的余数对应的数就是最终的 MEX 。

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainders = [0] * value
        for num in nums:
            remainders[num % value] += 1
        mincnt = min(remainders)
        minidx = remainders.index(mincnt)
        return mincnt * value + minidx
    
if __name__ == "__main__":
    s = Solution()
    print(s.findSmallestInteger([1,-10,7,13,6,8], 5))
    print(s.findSmallestInteger([1,2,3,5,7], 2))