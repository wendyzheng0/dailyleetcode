from typing import List
from collections import defaultdict


###
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
# 给定整数 capacity 和一个数组 trips ,  trips[i] = [numPassengersi, fromi, toi] 表示第 i 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
#
# 建立查分数组，然后遍历求每个时刻的乘客数量，如果超过capacity则返回False。
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        req = defaultdict(int)
        for num, dfrom, dto in trips:
            req[dfrom] += num
            req[dto] -= num
        curreq = 0
        for d in sorted(req):
            curreq += req[d]
            if curreq > capacity:
                return False
        return True
