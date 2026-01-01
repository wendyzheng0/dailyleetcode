from typing import List


###
# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重叠 。
# 注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。
#
# 贪心算法。按照结束时间排序，然后遍历每一个区间，如果当前区间的开始时间小于上一个区间的结束时间，则删除当前区间。
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        cnt = index = 0
        n = len(intervals)
        while index < n:
            start, end = intervals[index]
            cnt += 1
            index += 1
            while index < n and intervals[index][0] < end:
                index += 1
        return n - cnt
