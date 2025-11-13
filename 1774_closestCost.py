from typing import List
from bisect import bisect_left
from math import inf


###
# 你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。而制作甜点需要遵循以下几条规则：
# 必须选择 一种 冰激凌基料。
# 可以添加 一种或多种 配料，也可以不添加任何配料。
# 每种类型的配料 最多两份 。
# 给你以下三个输入：
# baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。
# toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。
# target ，一个整数，表示你制作甜点的目标价格。
# 你希望自己做的甜点总成本尽可能接近目标价格 target 。
# 返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。
#
# 受之前影响，虽然取值范围有10000，还是写了个dp（closestCost1）。速度十分慢。后来发现对于每种base来说topping
# 都是一样的，所以topping的取值组合只需要计算一次，用了个set来记录。然后转化为有序数组，方便遍历每种base的时候查询。
# 这样就快很多了。
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        dp = set({0})
        for topping in toppingCosts:
            for k in list(dp):
                dp.add(k + topping)
                dp.add(k + topping * 2)
        dp = sorted(list(dp))
        # print(dp)
        res = inf
        for base in baseCosts:
            subtarget = max(target - base, 0)
            idx = bisect_left(dp, subtarget)
            if idx < len(dp) and subtarget == dp[idx]:
                nearest = subtarget
            else:
                nearest = dp[idx - 1]
                if idx < len(dp) and subtarget - nearest > dp[idx] - subtarget:
                    nearest = dp[idx]
            nearest += base
            # print(f"base:{base}, nearest:{nearest}")
            if abs(nearest - target) < abs(res - target):
                res = nearest
            elif abs(nearest - target) == abs(res - target):
                res = min(res, nearest)
        return res

    def closestCost1(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        maxval = sum(toppingCosts) * 2
        dp = [True] + [False] * maxval
        for topping in toppingCosts:
            for j in range(maxval, topping - 1, -1):
                dp[j] |= dp[j - topping]
                if j >= topping * 2:
                    dp[j] |= dp[j - topping * 2]
        # for i in range(maxval + 1):
        #     if dp[i]:
        #         print(i)
        res = inf
        for base in baseCosts:
            subtarget = max(target - base, 0)
            nearest = inf
            for j in range(subtarget, maxval + 1):
                if dp[j]:
                    nearest = j
                    break
            for j in range(min(subtarget, maxval), -1, -1):
                if dp[j]:
                    if nearest - subtarget >= subtarget - j:
                        nearest = j
                    break
            nearest += base
            # print(f"base:{base}, nearest:{nearest}")
            if abs(nearest - target) < abs(res - target):
                res = nearest
            elif abs(nearest - target) == abs(res - target):
                res = min(res, nearest)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.closestCost([1,7], [3,4], 10))  # Expected: 10
    print(solution.closestCost([2,3], [4,5,100], 18))  # Expected: 17
    print(solution.closestCost([3,10], [2,5], 9))  # Expected: 8
    print(solution.closestCost([10], [1], 1))  # Expected: 10
    print(solution.closestCost([3], [3], 9))  # Expected: 9
    print(solution.closestCost([8,4,4,5,8], [3,10,9,10,8,10,10,9,3], 6))  # Expected: 5
    print(solution.closestCost([3,2], [3], 10))  # Expected: 9
    print(solution.closestCost([3738,5646,197,7652], [5056], 9853))  # Expected: 10309