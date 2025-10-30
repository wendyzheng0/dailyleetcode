from typing import List
from itertools import pairwise


###
# 给你一个整数数组 target 和一个数组 initial ，initial 数组与 target  数组有同样的维度，且一开始全部为 0 。
# 请你返回从 initial 得到  target 的最少操作次数，每次操作需遵循以下规则：
# 在 initial 中选择 任意 子数组，并将子数组中每个元素增加 1 。
# 答案保证在 32 位有符号整数以内。
#
# 对于答案来说，方法很简单，但是却很难想到这个方法。
# 最开始自己想的方法minNumberOperations1：对于一个山峰来说，需要的操作次数是山峰到山脚的高度差，所以中间的点都不重要，于是第一段
# 代码整理出了一个只包含山峰和山谷的点shorten。然后遍历每一座山，每遇到一个山顶到山脚的过程，就需要增加这段距离差次操作，相当于把这座
# 山削平了。
# 后来看了灵神的解答有了第二个方法minNumberOperations2：差方。先建立差方数组，第0个元素为target[0]，第i个元素为target[i]-target[i-1]。
# 每一次对子数组[i, j]的操作相当于在差方数组里面diff[i]+1和diff[j+1]-1。当j=n-1时，差方数组里面只有一个数加了1. initial最开始
# 差方数组是全0，操作过程就是把它变成target的差方数组的过程。对于每次操作，必然会有一个数被加1，所以差方数组里面所有数的和就是操作次数。
# 官方的解答是minNumberOperations：如果前一个数比后一个数小，那么需要额外的操作次数，否则不需要。
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = pre = 0
        for num in target:
            if num > pre:
                res += num - pre
            pre = num
        return res

    def minNumberOperations2(self, target: List[int]) -> int:
        return target[0] + sum(max(0, y - x) for x, y in pairwise(target))

    def minNumberOperations1(self, target: List[int]) -> int:
        shorten = [target[0]]
        for num in target:
            if num == shorten[-1]:
                continue
            if len(shorten) == 1:
                shorten.append(num)
            else:
                if shorten[-2] < shorten[-1] < num:
                    shorten[-1] = num
                elif shorten[-2] > shorten[-1] > num:
                    shorten[-1] = num
                else:
                    shorten.append(num)
        n = len(shorten)
        idx = 0
        res = 0
        pre = 0
        while idx + 1 < n:
            if shorten[idx] > shorten[idx + 1]:
                res += shorten[idx] - shorten[idx + 1]
                pre = shorten[idx + 1]
                idx += 2
            else:
                idx += 1
        if idx < n:
            res += max(pre, shorten[idx])
        else:
            res += pre
        return res
