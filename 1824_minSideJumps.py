from typing import List


###
# 给你一个长度为 n 的 3 跑道道路 ，它总共包含 n + 1 个 点 ，编号为 0 到 n 。一只青蛙从 0 号点第二条跑道 出发 ，它想要跳到点 n 处。然而道路上可能有一些障碍。
# 给你一个长度为 n + 1 的数组 obstacles ，其中 obstacles[i] （取值范围从 0 到 3）表示在点 i 处的 obstacles[i] 跑道上有一个障碍。如果 obstacles[i] == 0 ，那么点 i 处没有障碍。任何一个点的三条跑道中 最多有一个 障碍。
# 比方说，如果 obstacles[2] == 1 ，那么说明在点 2 处跑道 1 有障碍。
# 这只青蛙从点 i 跳到点 i + 1 且跑道不变的前提是点 i + 1 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 同一个 点处 侧跳 到 另外一条 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。
# 比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。
# 这只青蛙从点 0 处跑道 2 出发，并想到达点 n 处的 任一跑道 ，请你返回 最少侧跳次数 。
# 注意：点 0 处和点 n 处的任一跑道都不会有障碍。
#
# 记录每个点上到达每条跑道的最小侧跳次数。然后遍历每个点最后一个点上侧跳数最少的就是答案。
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        pre = [1, 0, 1]
        cur = [0] * 3
        preob = obstacles[0]
        for i in range(1, len(obstacles)):
            ob = obstacles[i]
            for j in range(3):
                if pre[j] != -1 and ob - 1 != j:
                    cur[j] = pre[j]
            if ob != 0:
                cur[ob - 1] = -1
            if preob != 0 and ob != preob:
                idx = preob - 1
                if cur[(idx + 1) % 3] < 0:
                    cur[idx] = cur[idx - 1] + 1
                elif cur[idx - 1] < 0:
                    cur[idx] = cur[(idx + 1) % 3] + 1
                else:
                    cur[idx] = min(cur[(idx + 1) % 3], cur[idx - 1]) + 1
            preob = ob
            pre, cur = cur, pre
            # print(pre)
        return min(pre)
