from typing import List
from functools import cache
from math import inf


###
# 给你两个长度为 n 下标从 0 开始的整数数组 cost 和 time ，分别表示给 n 堵不同的墙刷油漆需要的开销和时间。你有两名油漆匠：
# 一位需要 付费 的油漆匠，刷第 i 堵墙需要花费 time[i] 单位的时间，开销为 cost[i] 单位的钱。
# 一位 免费 的油漆匠，刷 任意 一堵墙的时间为 1 单位，开销为 0 。但是必须在付费油漆匠 工作 时，免费油漆匠才会工作。
# 请你返回刷完 n 堵墙最少开销为多少。
#
# 这题太难定义状态了。一开始的时候想用f[i][j]=(t,c)表示前i面墙选j面付费刷，花费t时间和c钱。后来发现很难写。
# 看了灵神的题解转换成0-1背包问题，真是妙啊，太难想了。
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        # 付费刷墙时间和 <= n - 付费刷墙个数 -> sigma（付费刷墙时间+1）<= n
        # 问题变成从n面墙里面选择x面墙付费刷时，花费最小是多少
        # 从time[i]+1, 0<=i<n个元素里面选择x个，使得cost[i](i属于x)的和最小
        # dfs(i,j):在前i个元素里面余量还有j时的最小花费，根据第i个元素选不选有下面式子：
        # dfs(i,j) = min(dfs(i-1,j-(time[i] + 1)) + cost[i], dfs(i-1, j))
        # dfs(n-1, n)为入口，j <= 0时，返回0，i < 0时，返回无穷大。

        @cache
        def dfs(i, j):
            if j <= 0:
                return 0
            if i < 0:
                return inf
            return min(dfs(i - 1, j - (time[i] + 1)) + cost[i], dfs(i - 1, j))
        return dfs(n - 1, n)
