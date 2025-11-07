from typing import List


###
# 给你一个下标从 0 开始长度为 n 的整数数组 stations ，其中 stations[i] 表示第 i 座城市的供电站数目。
# 每个供电站可以在一定 范围 内给所有城市提供电力。换句话说，如果给定的范围是 r ，在城市 i 处的供电站可以给所有满足 |i - j| <= r 且 0 <= i, j <= n - 1 的城市 j 供电。
# |x| 表示 x 的 绝对值 。比方说，|7 - 5| = 2 ，|3 - 10| = 7 。
# 一座城市的 电量 是所有能给它供电的供电站数目。
# 政府批准了可以额外建造 k 座供电站，你需要决定这些供电站分别应该建在哪里，这些供电站与已经存在的供电站有相同的供电范围。
# 给你两个整数 r 和 k ，如果以最优策略建造额外的发电站，返回所有城市中，最小电量的最大值是多少。
# 这 k 座供电站可以建在多个城市。
#
# 想了很多种策略没法找出最优的选择新建电站的城市的方案。看了灵神的解答豁然开朗，既然没有有效策略，那就用搜索的方式。因为
# 新建电站的城市的数量是有限的，所以可以用二分法来找到最小电量的最大值。因为小于答案的值肯定也能建出来，而大于答案的值肯定是
# 建不出来的。在检查某个值是否可以建出来的时候，由于不需要考虑最优结果，只需要用贪心的方法，从左到右检查每个城市，遇到城市
# 电量小于目标的时候，就在这个城市+r的城市建一个电站，使得这个城市和后面2r个城市都增加了target-num的电量。再继续检查后面的城市。
# 这里可以用查分数组来计算变化量，从而避免每次都要用O(r)的时间来更新电量。
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n
        power[0] = sum(stations[:r + 1])
        for i in range(1, n):
            power[i] = power[i - 1]
            power[i] += stations[i + r] if i + r < n else 0
            power[i] -= stations[i - r - 1] if i - r >= 1 else 0
        diff = [power[0]] + [power[i] - power[i - 1] for i in range(1, n)]

        def check(target):
            num = p = 0
            tmpdiff = diff.copy()
            for i in range(n):
                num += tmpdiff[i]
                if num < target:
                    add = target - num
                    tmpdiff[i] += add
                    if i + r * 2 + 1 < n:
                        tmpdiff[i + r * 2 + 1] -= add
                    p += add
                    num += add
                    if p > k:
                        # print(f"check {target}, fail")
                        return False
            # print(f"check {target}, pass")
            return True

        left = min(power) + k // n
        right = min(power) + k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            # print(f"left:{left}, right:{right}, mid:{mid}")
            if check(mid):
                left = mid
            else:
                right = mid
        return left
