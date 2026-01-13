from typing import List
from heapq import heappush, heappop


###
# 给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具 竞争力 的 nums 子序列。
# 数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
# 在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，那么我们称子序列 a 比子序列 b（相同长度下）更具 竞争力 。 例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。
#
# 方法mostCompetitive1：从前到后一个一个选择数字。第一个从nums[:n-k+1]中选最小的，第二个从nums[idx1:n-k+2]中选最小的，idx1是第一个数的索引。
# 这个方法每次会算最小的比较慢。于是看到了第二个方法mostCompetitive：遍历每个数字，如果当前数字比堆顶数字小，而且还可以删除更多的数字，那就把堆顶删掉。
# 直到不能再删了或者堆顶数字比当前数字小了。当前数字入栈。这样得到一个字典序最小的子序列。如果长度太长需截断。
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        totalrm = len(nums) - k
        res = []
        for val in nums:
            while totalrm and res and res[-1] > val:
                res.pop()
                totalrm -= 1
            res.append(val)
        return res[:len(res)-totalrm]

    def mostCompetitive1(self, nums: List[int], k: int) -> List[int]:
        start = 0
        res = []
        n = len(nums)
        if n == k:
            return nums
        # print(f"n:{n}, k:{k}")
        pq = []
        for i in range(n - k):
            heappush(pq, (nums[i], i))
        for i in range(n - k, n):
            heappush(pq, (nums[i], i))
            while pq[0][1] < start:
                heappop(pq)
            val, idx = heappop(pq)
            res.append(val)
            start = idx + 1
        return res
