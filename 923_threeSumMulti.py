from typing import List
from collections import Counter
from bisect import bisect_left, bisect_right


###
# 给定一个整数数组 arr ，以及一个整数 target 作为目标值，返回满足 i < j < k 且 arr[i] + arr[j] + arr[k] == target 的元组 i, j, k 的数量。
# 由于结果会非常大，请返回 10^9 + 7 的模。
#
# 开始的时候是尝试枚举每个值，能过，但很慢。后来就改成统计各个数字出现次数，然后在枚举有相等数字的情况和没有相等数字的情况。
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 1_000_000_007
        cnt = Counter(arr)
        # print(cnt)
        nums = sorted(cnt.keys())
        res = 0
        n = len(nums)
        # nums[i] < nums[j] < nums[k]
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                tmp = target - nums[i] - nums[j]
                if tmp <= nums[j]:
                    break
                if tmp in cnt:
                    res += cnt[nums[i]] * cnt[nums[j]] * cnt[tmp]
        # >=2 of them equal
        for i in range(n):
            tmp = target - nums[i] * 2
            if tmp in cnt:
                if tmp == nums[i]:
                    res += cnt[tmp] * (cnt[tmp] - 1) * (cnt[tmp] - 2) // 6
                else:
                    res += cnt[tmp] * cnt[nums[i]] * (cnt[nums[i]] - 1) // 2
        return res % MOD


    def threeSumMulti1(self, arr: List[int], target: int) -> int:
        MOD = 1_000_000_007
        arr.sort()
        n = len(arr)
        res = 0
        for i in range(n - 2):
            k = n
            for j in range(i + 1, n - 1):
                if j >= k:
                    break
                tmp = target - arr[i] - arr[j]
                startk = bisect_left(arr, tmp, j + 1, k)
                if startk >= n or arr[startk] != tmp:
                    continue
                endk = bisect_right(arr, tmp, startk, k)
                res = (res + endk - startk) % MOD
                k = endk
        return res
