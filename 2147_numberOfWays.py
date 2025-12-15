###
# 在一个图书馆的长廊里，有一些座位和装饰植物排成一列。给你一个下标从 0 开始，长度为 n 的字符串 corridor ，它包含字母 'S' 和 'P' ，其中每个 'S' 表示一个座位，每个 'P' 表示一株植物。
# 在下标 0 的左边和下标 n - 1 的右边 已经 分别各放了一个屏风。你还需要额外放置一些屏风。每一个位置 i - 1 和 i 之间（1 <= i <= n - 1），至多能放一个屏风。
# 请你将走廊用屏风划分为若干段，且每一段内都 恰好有两个座位 ，而每一段内植物的数目没有要求。可能有多种划分方案，如果两个方案中有任何一个屏风的位置不同，那么它们被视为 不同 方案。
# 请你返回划分走廊的方案数。由于答案可能很大，请你返回它对 109 + 7 取余 的结果。如果没有任何方案，请返回 0 。
#
# 找出所有在两组座位中间的植物数目，对于每一个植物数v可以有v+1种划分方案。
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = len(corridor)
        start = seat = 0
        while start < n and seat < 2:
            if corridor[start] == 'S':
                seat += 1
            start += 1
        if seat < 2:
            return 0
        plants = []
        i = start
        while i < n:
            nextseat = corridor.find('S', i)
            if nextseat >= 0:
                plants.append(nextseat - i)
                nextseat = corridor.find('S', nextseat + 1)
                if nextseat >= 0:
                    i = nextseat + 1
                else:
                    return 0
            else:
                break
        MOD = 1_000_000_007
        res = 1
        for v in plants:
            res = (res * (v + 1)) % MOD
        return res
