from typing import List


###
# 给你一个整数数组 nums 和一个 正 整数 k 。
# 定义长度为 2 * x 的序列 seq 的 值 为：
# (seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1]).
# 请你求出 nums 中所有长度为 2 * k 的 子序列 的 最大值 。
#
# 这题是有点麻烦的动态规划，很容易写错。先让cursor尝试写，结果只写了一个会超时的算法。让他改成用动态规划，结果就不干了，
# 重试了两次还是没有给我任何回复。最后还是自己写了。
# 灵神的题解都是从大到小遍历，我看着不习惯，按照自己习惯写了一遍。先计算[0,i]个数中选择[1,k]个数所有可能得到的OR sum，
# 然后计算[i,n-1]个数中选择[1,k]个数所有可能得到的OR sum，最后两两配对遍历所有可能的组合，计算最大值。
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [None] * n
        # all possible OR sum when select 0...k numbers from nums[0,i]
        f = [set() for _ in range(k + 1)]
        f[0].add(0)
        for i in range(n - k):
            # now f[j](f[i-1][j]) is all possible OR sum when selecting j (j = 0...k) numbers from nums[0, i-1]
            # next f[j](f[i][j]) = f[i-1][j] | {v | nums[i] for v in f[i-1][j-1]}
            for j in range(k, 0, -1):
                f[j].update(nums[i] | v for v in f[j - 1])
            pre[i] = f[k].copy()

        res = 0
        # all possible OR sum when select 0...k numbers from nums[i,n-1]
        f = [set() for _ in range(k + 1)]
        f[0].add(0)
        for i in range(n - 1, k - 1, -1):
            # f[j](f[i+1][j]) is all possible OR sum when selecting j (j=0...k) numbers from nums[i,n-1]
            # next f[j](f[i][j]) = f[i+1][j] | {v|nums[i] for v in f[i+1][j-1]}
            for j in range(k, 0, -1):
                f[j].update(nums[i] | v for v in f[j - 1])
            if i > n - k:
                continue
            # print(f"i:{i}, f[k]:{f[k]}, pre[i-1]:{pre[i-1]}")
            for s in f[k]:
                for p in pre[i - 1]:
                    res = max(res, s ^ p)
        return res


# 测试用例
if __name__ == "__main__":
    sol = Solution()
    
    # 示例 1
    nums1 = [2, 6, 7]
    k1 = 1
    print(f"示例 1: nums = {nums1}, k = {k1}")
    print(f"输出: {sol.maxValue(nums1, k1)}")  # 期望输出: 5
    print()
    
    # 示例 2
    nums2 = [4, 2, 5, 6, 7]
    k2 = 2
    print(f"示例 2: nums = {nums2}, k = {k2}")
    print(f"输出: {sol.maxValue(nums2, k2)}")  # 期望输出: 2
    print()

    # 示例 3
    nums3 = [16,83,31,113]
    k3 = 1
    print(f"示例 3: nums = {nums3}, k = {k3}")
    print(f"输出: {sol.maxValue(nums3, k3)}")  # 期望输出: 110

