from typing import List
from bisect import bisect_left


###
# 给你一个下标从 0 开始的二维整数数组 events ，其中 events[i] = [startTimei, endTimei, valuei] 。第 i 个活动开始于 startTimei ，结束于 endTimei ，如果你参加这个活动，那么你可以得到价值 valuei 。你 最多 可以参加 两个时间不重叠 活动，使得它们的价值之和 最大 。
# 请你返回价值之和的 最大值 。
# 注意，活动的开始时间和结束时间是 包括 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 t ，那么下一个活动必须在 t + 1 或之后的时间开始。
#
# 所有事件按照结束时间排序。然后遍历时检查开始时间前可以获得的最大价值，更新最大价值。然后根据需要更新当前结束时间的最大价值。
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        maxval = dict()
        maxendtime = []
        events.sort(key=lambda x: x[1])
        res = max(x[2] for x in events)
        for start, end, value in events:
            p = bisect_left(maxendtime, start)
            if p > 0:
                res = max(res, maxval[maxendtime[p - 1]] + value)
            if not maxendtime:
                maxendtime.append(end)
                maxval[end] = value
            elif maxval[maxendtime[-1]] < value:
                if end != maxendtime[-1]:
                    maxendtime.append(end)
                maxval[end] = value
        # print(f"sorted: {events}")
        # print(maxendtime)
        # print(maxval)
        return res
