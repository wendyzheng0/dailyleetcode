from typing import List
from heapq import heappop, heappush, heapreplace


###
# 给你一个整数 n ，共有编号从 0 到 n - 1 的 n 个会议室。
# 给你一个二维整数数组 meetings ，其中 meetings[i] = [starti, endi] 表示一场会议将会在 半闭 时间区间 [starti, endi) 举办。所有 starti 的值 互不相同 。
# 会议将会按以下方式分配给会议室：
# 每场会议都会在未占用且编号 最小 的会议室举办。
# 如果没有可用的会议室，会议将会延期，直到存在空闲的会议室。延期会议的持续时间和原会议持续时间 相同 。
# 当会议室处于未占用状态时，将会优先提供给原 开始 时间更早的会议。
# 返回举办最多次会议的房间 编号 。如果存在多个房间满足此条件，则返回编号 最小 的房间。
# 半闭区间 [a, b) 是 a 和 b 之间的区间，包括 a 但 不包括 b 。
#
# 在使用的会议室和空闲的会议室分开记录，一个按照会议结束时间排序，一个按照序号排序。按照开始时间从小到大遍历会议，每次先更新在使用的会议室有没有可以变成空闲的。
# 然后选择会议室。最后统计开会最多的会议室
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [(i, 0) for i in range(n)]
        inuse = []
        for start, end in meetings:
            while inuse and inuse[0][0] <= start:
                room = heappop(inuse)
                heappush(available, (room[1], room[2]))
            if not available:
                heapreplace(inuse, (end + inuse[0][0] - start, inuse[0][1], inuse[0][2] + 1))
            else:
                avlroom = heappop(available)
                heappush(inuse, (end, avlroom[0], avlroom[1] + 1))
            # print(f)
        while inuse:
            room = heappop(inuse)
            available.append((room[1], room[2]))
        return max(available, key=lambda x: (x[1], -x[0]))[0]
