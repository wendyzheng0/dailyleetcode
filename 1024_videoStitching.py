from typing import List


###
# 你将会获得一系列视频片段，这些片段来自于一项持续时长为 time 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
# 使用数组 clips 描述所有的视频片段，其中 clips[i] = [starti, endi] 表示：某个视频片段开始于 starti 并于 endi 结束。
# 甚至可以对这些片段自由地再剪辑：
# 例如，片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
# 我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, time]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。
#
# 贪心算法。按照结束时间排序，然后从后往前遍历，在可以覆盖当前结束时间的片段中选最小开始时间的片段，这个开始时间作为新的结束时间。
# 如果没有可以覆盖当前结束时间的片段，则返回-1。
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (-x[1], x[0]))
        idx = 0
        res = 0
        while time > 0:
            left = time
            while idx < len(clips) and clips[idx][1] >= time:
                left = min(left, clips[idx][0])
                idx += 1
            if left < time:
                res += 1
                time = left
            else:
                return -1
        return res
