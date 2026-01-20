from typing import List
from functools import cache


###
# 一张桌子上总共有 n 个硬币 栈 。每个栈有 正整数 个带面值的硬币。
# 每一次操作中，你可以从任意一个栈的 顶部 取出 1 个硬币，从栈中移除它，并放入你的钱包里。
# 给你一个列表 piles ，其中 piles[i] 是一个整数数组，分别表示第 i 个栈里 从顶到底 的硬币面值。同时给你一个正整数 k ，请你返回在 恰好 进行 k 次操作的前提下，你钱包里硬币面值之和 最大为多少 。
#
# 开始的时候一个个数字模拟从栈里面取出来，结果超时了。然后转变思路，分k次每次从任意栈里取硬币，相当于各个栈依次取一些硬币，总共取k个。这样遍历每个栈可能取的硬币个数就可以了。
# 开始的时候用递归maxValueOfCoins1加记忆化搜索，每次计算当前堆前i个硬币和还是超时，改成缓存s每次更新就过了。后来翻译成递推maxValueOfCoins，加了一个超过total就跳过更快一点。
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # dp[i][j] max value can get from first i piles select j times
        # dp[i][j] = max(dp[i - 1][x] + piles[i][:j - x]) 0<=x<=j
        dp = [0] * (k + 1)
        total = 0
        for pile in piles:
            cur = [0] * (k + 1)
            n = len(pile)
            total += n
            for i in range(min(k, n) - 1):
                pile[i + 1] += pile[i]
            pile = [0] + pile
            for x in range(k + 1):
                if x > total:
                    cur[x] = cur[x - 1]
                    continue
                v = 0
                for i in range(min(n, x) + 1):
                    v = max(pile[i] + dp[x - i], v)
                cur[x] = v
            dp, cur = cur, dp
            # print(dp)
        return max(dp)

    def maxValueOfCoins1(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        @cache
        def dfs(pileidx: int, r: int) -> int:
            if pileidx == n or r == 0:
                return 0
            ret = 0
            s = 0
            m = len(piles[pileidx])
            for i in range(min(r + 1, m + 1)):
                # value = sum(piles[pileidx][:i])
                ret = max(ret, dfs(pileidx + 1, r - i) + s)
                s += piles[pileidx][i] if i < m else 0
            return ret

        return dfs(0, k)
