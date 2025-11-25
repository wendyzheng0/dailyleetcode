from typing import List


###
# 给你一个长度为 n 下标从 0 开始的整数数组 maxHeights 。
# 你的任务是在坐标轴上建 n 座塔。第 i 座塔的下标为 i ，高度为 heights[i] 。
# 如果以下条件满足，我们称这些塔是 美丽 的：
# 1 <= heights[i] <= maxHeights[i]
# heights 是一个 山脉 数组。
# 如果存在下标 i 满足以下条件，那么我们称数组 heights 是一个 山脉 数组：
# 对于所有 0 < j <= i ，都有 heights[j - 1] <= heights[j]
# 对于所有 i <= k < n - 1 ，都有 heights[k + 1] <= heights[k]
# 请你返回满足 美丽塔 要求的方案中，高度和的最大值 。
#
# 这题用了类似接雨水的方法先从左到右遍历每个点，计算以该点为山峰时左边山脉所能获得的最大高度和left。
# 然后用类似方法从右到左计算每一个点为山峰时右边山脉的最大高度和right。最后再遍历每个点，该点作为山峰时
# 的最大高度和就是left[i] = right[i + 1]，求这里的最大值就是答案。
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        n = len(maxHeights)
        left = [0] * n
        stack = []
        for i, h in enumerate(maxHeights):
            while stack and maxHeights[stack[-1]] > h:
                del stack[-1]
            if not stack:
                left[i] = (i + 1) * h
            else:
                left[i] = (left[stack[-1]] + (i - stack[-1]) * h)
            stack.append(i)
        right = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            h = maxHeights[i]
            while stack and maxHeights[stack[-1]] > h:
                del stack[-1]
            if not stack:
                right[i] = (n - i) * h
            else:
                right[i] = (right[stack[-1]] + (stack[-1] - i) * h)
            stack.append(i)
        # print(left)
        # print(right)
        res = max(right[0], left[n - 1])
        for i in range(n - 1):
            res = max(res, left[i] + right[i + 1])
        return res
