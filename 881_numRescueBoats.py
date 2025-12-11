from typing import List
from collections import Counter


###
# 给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
# 返回 承载所有人所需的最小船数 。
#
# 贪心算法。先排序，然后从两边往中间走，如果两个人可以一起坐船，就一起，否则让体重最重的人坐船。
# 精细计算各种体重出现次数然后配对，反而比直接一个个遍历要慢。
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            res += 1
        return res

    def numRescueBoats1(self, people: List[int], limit: int) -> int:
        res = 0
        cnt = Counter(people)
        uniq = sorted(list(set(people)))
        while uniq:
            p = uniq.pop(-1)
            while cnt[p] > 0 and uniq:
                s = uniq[0]
                if s + p <= limit:
                    b = min(cnt[p], cnt[s])
                    cnt[p] -= b
                    cnt[s] -= b
                    res += b
                    if cnt[s] == 0:
                        uniq.pop(0)
                else:
                    break
            if cnt[p] > 0:
                if p * 2 <= limit:
                    res += cnt[p] // 2 + cnt[p] % 2
                else:
                    res += cnt[p]

        return res
