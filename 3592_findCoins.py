from typing import List


###
# 给你一个 从 1 开始计数 的整数数组 numWays，其中 numWays[i] 表示使用某些 固定 面值的硬币（每种面值可以使用无限次）凑出总金额 i 的方法数。每种面值都是一个 正整数 ，并且其值 最多 为 numWays.length。
# 然而，具体的硬币面值已经 丢失 。你的任务是还原出可能生成这个 numWays 数组的面值集合。
# 返回一个按从小到大顺序排列的数组，其中包含所有可能的 唯一 整数面值。
# 如果不存在这样的集合，返回一个 空 数组。
#
# 用动态规划的方法一边遍历numWays，一边记录已经选择的coins组成对应面值的组合数。
# 当当前面值组合数和期待的一样，跳过。
# 当发现当前面值的组合数比期待的少1时，增加该面值到coins，并更新后续面值的组合数。
# 其他情况说明不存在这样的集合，返回空数组。
class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        dp = [1] + [0] * n
        coins = []
        # tell enumerate index starts from 1
        for v, w in enumerate(numWays, 1):
            if w == dp[v]:
                continue
            elif w == dp[v] + 1:
                coins.append(v)
                for j in range(v, n + 1):
                    dp[j] += dp[j - v]
            else:
                return []
        return coins
