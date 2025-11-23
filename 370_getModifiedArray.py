from typing import List


###
# 假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。
# 其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
# 请你返回 k 次操作后的数组。
#
# 用查分数组把每次操作的复杂度变为O(1)。最后对查分数组求前缀和就是最终结果。注意去掉差分数组的最后一个元素。
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)
        for startidx, endidx, inc in updates:
            diff[startidx] += inc
            diff[endidx + 1] -= inc
            # print(diff)
        for i in range(length):
            diff[i + 1] = diff[i + 1] + diff[i]
        return diff[:-1]
