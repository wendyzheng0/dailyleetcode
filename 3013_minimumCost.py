from bisect import bisect_left
from typing import List

###
# 给你一个下标从 0 开始长度为 n 的整数数组 nums 和两个 正 整数 k 和 dist 。
# 一个数组的 代价 是数组中的 第一个 元素。比方说，[1,2,3] 的代价为 1 ，[3,4,1] 的代价为 3 。
# 你需要将 nums 分割成 k 个 连续且互不相交 的子数组，满足 第二 个子数组与第 k 个子数组中第一个元素的下标距离 不超过 dist 。换句话说，如果你将 nums 分割成子数组 nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)] ，那么它需要满足 ik-1 - i1 <= dist 。
# 请你返回这些子数组的 最小 总代价。
#
# 第一个数字是必须要的，之后的代价就是长度为dist+1的子数组的前k-1小数字的和。用了一个有序数组来维护中间的数字。
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        cand = nums[1:dist + 2]
        cand.sort()
        res = arrsum = sum(cand[:k - 1])
        # print(f"{cand}, {arrsum}")
        for i in range(dist + 2, len(nums)):
            out = nums[i - dist - 1]
            outpos = bisect_left(cand, out)
            # print(f"{out}, {outpos}")
            if outpos <= k - 2:
                arrsum -= out
            del cand[outpos]
            inpos = bisect_left(cand, nums[i])
            cand.insert(inpos, nums[i])
            # print(f"{nums[i]}, {inpos}")
            if outpos <= k - 2:
                if inpos <= k - 2:
                    arrsum += nums[i]
                else:
                    arrsum += cand[k - 2]
            elif inpos <= k - 2:
                    arrsum += nums[i] - cand[k - 1]
            if res > arrsum:
                res = arrsum
            # print(f"{cand}, {arrsum}")
        return res + nums[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumCost([1,3,2,6,4,2], 3, 3)) # 5
    print(sol.minimumCost([10,1,2,2,2,1], 4, 3)) # 15
    print(sol.minimumCost([10,8,18,9], 3, 1)) # 36
    print(sol.minimumCost([1,6,4,7,9,6,1], 4, 4)) # 12
    print(sol.minimumCost([2,6,3,8,3,1,1], 3, 4)) # 4
