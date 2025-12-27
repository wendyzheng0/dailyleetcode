from typing import List


###
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
# 先递归找出所有可能的子集，然后递归检查各个子集是否有交集，没有交集就尝试选择作为组合，直到找到合法组合。
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        target = s // k
        n = len(nums)
        nums.sort()
        if nums[-1] > target:
            return False
        validsubset = []

        def dfs(idx, val, mask):
            if val == 0:
                validsubset.append(mask)
                return
            for i in range(idx, n):
                if val < nums[i]:
                    break
                dfs(i + 1, val - nums[i], mask | 1 << i)
            return

        dfs(0, target, 0)

        m = len(validsubset)

        def checkcom(idx, mask):
            if mask & (mask + 1) == 0 and bin(mask).count('1') == n:
                return True
            for i in range(idx, m):
                if mask & validsubset[i] == 0:
                    ret = checkcom(i + 1, mask | validsubset[i])
                    if ret:
                        return ret
            return False

        return checkcom(0, 0)



if __name__ == "__main__":
    sol = Solution()
    print(sol.canPartitionKSubsets([4,3,2,3,5,2,1], 4)) # True
    print(sol.canPartitionKSubsets([1, 2, 3, 4], 3)) # False
    print(sol.canPartitionKSubsets([1,1,2,2,2], 3)) # False
    print(sol.canPartitionKSubsets([114,96,18,190,207,111,73,471,99,20,1037,700,295,101,39,649], 4)) # True
