from typing import List


###
# 你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。
# 你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
# 你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
# 你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
# 一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
# 给你一个整数数组 fruits ，返回你可以收集的水果的 最大 数目。
#
# 遍历水果数组，记录前一种水果种类，个数和当前水果种类和个数，如果新遇到一种水果则计算前两种水果数目，更新最大值。如果下一种水果跟前一种水果一样，累积当前水果个数并更新当前种类为前一种类。
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        pretype = -1
        precnt = 0
        curtype = fruits[0]
        curcnt = 0
        for i, t in enumerate(fruits):
            if t == curtype:
                curcnt += 1
            else:
                res = max(res, precnt + curcnt)
                if pretype == t:
                    precnt += curcnt
                else:
                    precnt = curcnt
                pretype = curtype
                curtype = t
                curcnt = 1
        return max(res, precnt + curcnt)
