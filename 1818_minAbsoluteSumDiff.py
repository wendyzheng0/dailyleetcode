from typing import List
from bisect import bisect_left


###
# 给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。
# 数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。
# 你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。
# 在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
# |x| 定义为：
# 如果 x >= 0 ，值为 x ，或者
# 如果 x <= 0 ，值为 -x
#
# 先计算各个绝对差值，按照从大到小的顺序计算当前绝对差值最大可以减少多少。取可以减少最多的那个，计算新的绝对差值和。
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sortednums1 = sorted(nums1)
        diff = sorted([(abs(n1 - n2), idx) for idx, (n1, n2) in enumerate(zip(nums1, nums2))], reverse=True)
        # print(sortednums1)
        # print(diff)
        diffsum = sum(v for v, idx in diff)
        # max diff can reduce after switch
        maxreduce = 0
        for diffval, idx in diff:
            if diffval <= maxreduce:
                break
            # find closest num in nums1 for nums2[idx]
            pos = bisect_left(sortednums1, nums2[idx])
            newdiff = abs(nums2[idx] - sortednums1[pos - 1])
            if pos < len(sortednums1):
                newdiff = min(newdiff, abs(nums2[idx] - sortednums1[pos]))
            # print(f"idx:{idx}, newdiff:{newdiff}, pos:{pos}")
            if maxreduce < (diffval - newdiff):
                maxreduce = diffval - newdiff
        return (diffsum - maxreduce) % 1_000_000_007
