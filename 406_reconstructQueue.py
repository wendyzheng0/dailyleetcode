from typing import List


###
# 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
# 请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。
#
# 一种方法是从高到矮排序，先安排高的。
# 另一种方法是倒过来。
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res

    def reconstructQueue1(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort(key=lambda x: (x[0], -x[1]))
        res = [None] * n
        for h, k in people:
            spaces = k + 1
            for j in range(n):
                if res[j] is None:
                    spaces -= 1
                    if spaces == 0:
                        res[j] = [h, k]
                        # print(f"[{h},{k}] put in res[{j}]")
                        break
        return res
