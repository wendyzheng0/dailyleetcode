from typing import List


###
# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
# 你必须找到一个内存复杂度优于 O(n2) 的解决方案。
#
# 开始尝试分块，发现还是逃不过n^2的复杂度。看了灵神的解答，才知道可以用二分查找来解决。
# 查找有多少个数字小于等于x值需要2n的复杂度，而最大值和最小值是可以直接从matrix里面得到的。
# 当x越大，matrix里面小于x的数字越多，反之越少，所以可以用二分查找来找第k小的数字。
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def smallernum(x):
            i, j = 0, n - 1
            res = 0
            while i < n and j >= 0:
                if matrix[i][j] <= x:
                    res += j + 1
                    i += 1
                else:
                    j -= 1
            return res

        left, right = matrix[0][0] - 1, matrix[n - 1][n - 1]
        while left < right:
            mid = (left + right) // 2
            z = smallernum(mid)
            print(f"left:{left}, right:{right}, z:{z}")
            if z >= k:
                right = mid
            else:
                left = mid + 1
        return right
