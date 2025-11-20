from typing import List


###
# 给你一个二维整数数组 intervals ，其中 intervals[i] = [starti, endi] 表示从 starti 到 endi 的所有整数，包括 starti 和 endi 。
# 包含集合 是一个名为 nums 的数组，并满足 intervals 中的每个区间都 至少 有 两个 整数在 nums 中。
# 例如，如果 intervals = [[1,3], [3,7], [8,9]] ，那么 [1,2,4,7,8,9] 和 [2,3,4,8,9] 都符合 包含集合 的定义。
# 返回包含集合可能的最小大小。
#
# 用贪心的算法。先把intervals按照end排序，然后遍历每一个interval的时候，检查nums里面有没有在范围里的数了，如果没有，
# 尽量取最靠近右边的整数加入nums。
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # print(intervals)
        prestart, preend = intervals[0]
        nums = [preend - 1, preend]
        for start, end in intervals:
            if nums[-1] < start:
                nums.append(end - 1)
                nums.append(end)
            elif nums[-1] == start:
                nums.append(end)
            elif nums[-2] < start:
                if nums[-1] == end:
                    nums.insert(-1, end - 1)
                else:
                    nums.append(end)
        # print(nums)
        return len(nums)
