from typing import List
from heapq import heapify, heapreplace
import math


###
# 给你一个整数 mountainHeight 表示山的高度。
# 同时给你一个整数数组 workerTimes，表示工人们的工作时间（单位：秒）。
# 工人们需要 同时 进行工作以 降低 山的高度。对于工人 i :
# 山的高度降低 x，需要花费 workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x 秒。例如：
# 山的高度降低 1，需要 workerTimes[i] 秒。
# 山的高度降低 2，需要 workerTimes[i] + workerTimes[i] * 2 秒，依此类推。
# 返回一个整数，表示工人们使山的高度降低到 0 所需的 最少 秒数。
#
# minNumberOfSeconds是贪心，每次山的高度减1，选择工作完成后时间最小的工人，然后更新工人下次工作完的时间。
# minNumberOfSeconds1是二分。开始的时候还妄想用类似背包的动态规划，结果超时。后来发现当知道时间去求可以降低的
# 高度是比较容易的，而且时间越多，可以降低的高度越大，所以可以用二分来求解。
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # next: time after he finishes his work
        # delta: time increase for next after he finishes his work
        # base: time to finish first work
        heap = [[t, t + t, t] for t in workerTimes]
        heapify(heap)
        for i in range(mountainHeight):
            nxt, delta, base = heap[0]
            heapreplace(heap, [nxt + delta, delta + base, base])
        return nxt

    def minNumberOfSeconds1(self, mountainHeight: int, workerTimes: List[int]) -> int:
        n = len(workerTimes)
        maxT = max(workerTimes)
        h = math.ceil(mountainHeight / n)
        right = math.floor(maxT * h * (h + 1) / 2)
        left = 0
        while left < right:
            mid = (left + right) // 2
            totalh = 0
            for t in workerTimes:
                k = int(mid // t)
                totalh += math.floor((math.isqrt(1 + 8 * k) - 1) / 2)
            if totalh >= mountainHeight:
                right = mid
            else:
                left = mid + 1
        return right


if __name__ == "__main__":
    solution = Solution()
    print(solution.minNumberOfSeconds(4, [2,1,1])) # 3
    print(solution.minNumberOfSeconds1(10, [3,2,2,4])) # 12
    print(solution.minNumberOfSeconds(5, [1])) # 15
    print(solution.minNumberOfSeconds1(1, [2,1])) # 1
    print(solution.minNumberOfSeconds(1, [1])) # 1
    print(solution.minNumberOfSeconds1(100, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) # 1