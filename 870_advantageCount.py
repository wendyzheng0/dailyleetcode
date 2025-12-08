from typing import List


###
# 给定两个长度相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。
# 返回 nums1 的 任意 排列，使其相对于 nums2 的优势最大化。
#
# 开始的时候总是想着nums1从大到小遍历，使得nums1的数刚好对上nums2里面比它小的最大的数，这是解法advantageCount1，其实多了很多判断。
# 后来看了别人的解法可以从小到大遍历，如果nums2里找不到比它小的数，就让它对应nums2里面最大的没有对应的数。因为哪怕nums1里有其他数比
# 这个最大的数大，考虑到nums2里剩下的数都比这个数小，那个数肯定也可以在剩余的数里面找到能对应的数。
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()
        idx = sorted(range(n), key=lambda x: nums2[x])
        res = [0] * n
        small, large = 0, n - 1
        for v in nums1:
            if nums2[idx[small]] >= v:
                res[idx[large]] = v
                large -= 1
            else:
                res[idx[small]] = v
                small += 1
        return res

    def advantageCount1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = sorted(enumerate(nums1), key=lambda x: x[1], reverse=True)
        snums2 = sorted(enumerate(nums2), key=lambda x: x[1], reverse=True)
        n = len(nums2)
        p = q = 0
        res = [-1] * n
        for i, v in snums1:
            while p < n and snums2[p][1] >= v:
                p += 1
            if p < n:
                res[snums2[p][0]] = v
                p += 1
            else:
                while q < n and res[q] != -1:
                    q += 1
                if q < n:
                    res[q] = v
        return res
