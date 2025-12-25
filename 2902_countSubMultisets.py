from typing import List
from collections import Counter


###
# 给你一个下标从 0 开始的非负整数数组 nums 和两个整数 l 和 r 。
# 请你返回 nums 中子多重集合的和在闭区间 [l, r] 之间的 子多重集合的数目 。
# 由于答案可能很大，请你将答案对 109 + 7 取余后返回。
# 子多重集合 指的是从数组中选出一些元素构成的 无序 集合，每个元素 x 出现的次数可以是 0, 1, ..., occ[x] 次，其中 occ[x] 是元素 x 在数组中的出现次数。
# 注意：
# 如果两个子多重集合中的元素排序后一模一样，那么它们两个是相同的 子多重集合 。
# 空 集合的和是 0 。
#
# 这题跟2585很像。用动态规划求解，由于每个数可以用的次数是有限的，常规动态规划求到的会超过限制，需要把超过部分减掉。由于有0的存在，f[0]则不止1中方案，而是
# cnt[0] + 1种方案。还有一个小优化是遍历的过程记录所有数字能组合出的最大值，这样就不一定要算到r了。
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        MOD = 1_000_000_007
        cnt = Counter(nums)
        f = [cnt[0] + 1] + [0] * r
        del cnt[0]
        maxval = 0
        for v, c in cnt.items():
            maxval = min(maxval + v * c, r)
            for i in range(v, maxval + 1):
                f[i] = (f[i] + f[i - v]) % MOD
            ex = v * (c + 1)
            for i in range(maxval, ex - 1, -1):
                f[i] = (f[i] - f[i - ex]) % MOD
            # print(f"{v},{c},{f}")
        return sum(f[l:]) % MOD


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubMultisets([1,2,2,3], 6, 6)) # Expected: 1
    print(sol.countSubMultisets([2,1,4,2,7], 1, 5)) # 7
    print(sol.countSubMultisets([1,2,1,3,5,2], 3, 5))   # Expected: 9
    print(sol.countSubMultisets([0,0,1,2,3], 2, 3))   # Expected: 9
    print(sol.countSubMultisets([3,1,1,3], 1, 1))   # Expected: 1
    print(sol.countSubMultisets([23,54,2,21,43,41,5,9,27,6,41,27,18,20,9,12,8,9,57,13,31,25,33,11,30,12,34,19,1,12,13,40,28,40,22,4,36,8,11,5,9,11,34,13,20,20,25,14,9,19,89,5,37,4,6,32,44,1,2,28,6,15,26,9,60,2,9,4,11,36,63,18,6,79,6,1,8,37,22,15,16,0,15,1,54,6,11,11,4,5,36,27,17,33,30,19], 122, 474))   # Expected: 391827978