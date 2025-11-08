from typing import List
from functools import cache
from collections import Counter
from math import inf


###
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
#
# 开始的时候用递归加记忆化搜索做的findMaxForm1。
# dfs(idx, leftm, leftn, length)表示前idx个字符串中最多有leftm个0和leftn个1的子集的最大长度。
# 如果选择当前字符串，则为dfs(idx + 1, leftm - zeros, leftn - ones, length + 1)。
# 否则为dfs(idx + 1, leftm, leftn, length)。
# 这个方法能过，但是太慢。学着改成动态规划的findMaxForm。
# f[i, m, n]表示前i个字符串可以组成m个0和n个1的子集的最大长度。
# 那么f[i, m, n] = max(f[i-1, m, n], f[i-1, m-zeros, n-ones] + 1)，其中zeros和ones是第i个字符串中0和1的个数。
# 对于每个字符串，需要更新f[i, x, y] (0 <= x <= m, 0 <= y <= n)的值。由于f十分稀疏，用dict来记录。
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = dict()
        for idx, s in enumerate(strs):
            cnt = Counter(s)
            zeros, ones = cnt['0'], cnt['1']
            cur = dp.copy()
            for mm, nn in dp.keys():
                if mm + zeros <= m and nn + ones <= n:
                    newkey = (mm + zeros, nn + ones)
                    if newkey not in cur:
                        cur[newkey] = dp[(mm, nn)] + 1
                    else:
                        cur[newkey] = max(cur[newkey], dp[(mm, nn)] + 1)
            if zeros <= m and ones <= n and (zeros, ones) not in cur:
                cur[(zeros, ones)] = 1
            dp = cur
        return max(dp.values()) if dp else 0

    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(idx, leftm, leftn, length):
            if idx >= len(strs):
                if leftm >= 0 and leftn >= 0:
                    return length
                else:
                    return -inf
            if leftm < 0 or leftn < 0:
                return -inf
            cnt = Counter(strs[idx])
            r1 = dfs(idx + 1, leftm, leftn, length)
            r2 = dfs(idx + 1, leftm - cnt['0'], leftn - cnt['1'], length + 1)
            return max(r1, r2)

        return dfs(0, m, n, 0)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxForm(["10","0001","111001","1","0"], 4, 3)) # 3
    print(sol.findMaxForm(["10","0","1"], 1, 1)) # 2
    print(sol.findMaxForm(["10","0001","111001","1","0"], 5, 3)) # 4
    print(sol.findMaxForm(["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"], 9, 80)) # 17
    print(sol.findMaxForm(["00","000"], 1, 10)) # 0