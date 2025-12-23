from typing import List


###
# 考试中有 n 种类型的题目。给你一个整数 target 和一个下标从 0 开始的二维整数数组 types ，其中 types[i] = [counti, marksi] 表示第 i 种类型的题目有 counti 道，每道题目对应 marksi 分。
# 返回你在考试中恰好得到 target 分的方法数。由于答案可能很大，结果需要对 109 +7 取余。
# 注意，同类型题目无法区分。
# 比如说，如果有 3 道同类型题目，那么解答第 1 和第 2 道题目与解答第 1 和第 3 道题目或者第 2 和第 3 道题目是相同的。
#
# 动态规划，dp[i]表示得到i分的方法数。由于同类题目没法区分而且有数量限制，需要遍历没有题目的时候尝试1～cnt题的情况。这是waysToReachTarget1
# 后来看到别人的更简洁方法waysToReachTarget，先计算可以做任意题的情况，再减去超出了cnt题的数量。
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [1] + [0] * target
        for cnt, mask in types:
            # use mask any times
            for i in range(mask, target + 1):
                dp[i] += dp[i - mask]
            # reduce use more than cnt times
            d = (cnt + 1) * mask
            for i in range(target, d - 1, -1):
                dp[i] -= dp[i - d]
        return dp[target] % 1_000_000_007

    def waysToReachTarget1(self, target: int, types: List[List[int]]) -> int:
        dp = [1] + [0] * target
        for cnt, mask in types:
            for j in range(target, mask - 1, -1):
                for i in range(mask, min((cnt + 1) * mask, j + 1), mask):
                    dp[j] += dp[j - i]
        return dp[target] % 1_000_000_007
