from typing import List
from collections import defaultdict
from itertools import pairwise


###
# 给你一个二维整数数组 squares ，其中 squares[i] = [xi, yi, li] 表示一个与 x 轴平行的正方形的左下角坐标和正方形的边长。
# 找到一个最小的 y 坐标，它对应一条水平线，该线需要满足它以上正方形的总面积 等于 该线以下正方形的总面积。
# 答案如果与实际答案的误差在 10-5 以内，将视为正确答案。
# 注意：正方形 可能会 重叠。重叠区域只 统计一次 。
#
# 跟3453仅仅差了一点，这一题的重叠区域只能算一次，因此对于被y分割的每一块不能用简单的查分数组来计算。
# 于是我在separateSquares用了两个数组分别记录增加的和减少的x区间，然后计算并记录每个y区间的面积。
# 得到了每个y区间的面积之后就跟3453一样了。separateSquares1是AI写的，竟然一次就通过，有点惊艳我了。
class Solution:
    def separateSquares1(self, squares: List[List[int]]) -> float:
        """
        使用扫描线算法处理重叠正方形，找到使上下面积相等的水平线y坐标
        
        思路：
        1. 将每个正方形的上下边界作为事件（进入/退出）
        2. 按y坐标排序事件，对每个y区间计算被覆盖的x轴长度
        3. 使用区间合并来处理x轴上的重叠
        4. 累加面积，找到使上下面积相等的精确y坐标
        """
        # 收集所有y事件: (y坐标, delta, x1, x2)
        # delta=+1 表示正方形进入，delta=-1 表示正方形退出
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))       # 下边界，进入
            events.append((y + l, -1, x, x + l))  # 上边界，退出
        
        events.sort()
        
        # 使用字典追踪每个x区间的活跃计数（处理相同区间多次出现的情况）
        interval_count = defaultdict(int)
        
        # 存储每个y区间的信息: (y_start, y_end, covered_width)
        areas = []
        prev_y = None
        
        i = 0
        while i < len(events):
            y = events[i][0]
            
            # 在处理当前y的事件之前，计算从prev_y到y的面积
            if prev_y is not None and prev_y < y:
                # 获取当前所有活跃的x区间
                active = [(x1, x2) for (x1, x2), cnt in interval_count.items() if cnt > 0]
                if active:
                    # 合并重叠区间
                    sorted_intervals = sorted(active)
                    merged = []
                    for interval in sorted_intervals:
                        if merged and interval[0] <= merged[-1][1]:
                            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
                        else:
                            merged.append(interval)
                    
                    covered_width = sum(r - l for l, r in merged)
                    areas.append((prev_y, y, covered_width))
            
            # 处理所有相同y坐标的事件
            while i < len(events) and events[i][0] == y:
                _, delta, x1, x2 = events[i]
                interval_count[(x1, x2)] += delta
                if interval_count[(x1, x2)] == 0:
                    del interval_count[(x1, x2)]
                i += 1
            
            prev_y = y
        
        # 计算总面积
        total_area = sum(width * (y_end - y_start) for y_start, y_end, width in areas)
        target = total_area / 2
        
        # 二分/累加查找使上下面积相等的y坐标
        cumsum = 0
        for y_start, y_end, width in areas:
            area = width * (y_end - y_start)
            if cumsum + area >= target:
                # 在这个区间内找到精确的y坐标
                needed = target - cumsum
                h = needed / width  # 需要的高度
                return y_start + h
            cumsum += area
        
        # 理论上不会到达这里
        return areas[-1][1] if areas else 0.0


    def separateSquares(self, squares: List[List[int]]) -> float:
        diff = dict()
        for x, y, l in squares:
            diff[y] = diff.get(y, ([], []))
            diff[y][0].append((x, x + l))
            diff[y + l] = diff.get(y + l, ([], []))
            diff[y + l][1].append((x, x + l))

        def gettotallength(sections: defaultdict) -> float:
            active = [item for item, cnt in sections.items() if cnt > 0]
            active.sort()
            sectionList = []
            for x1, x2 in active:
                if sectionList and sectionList[-1][1] >= x1:
                    sectionList[-1] = (sectionList[-1][0], max(sectionList[-1][1], x2))
                else:
                    sectionList.append((x1, x2))
            return sum(x2 - x1 for x1, x2 in sectionList)

        sections = defaultdict(int)
        areas = dict()
        for y, y1 in pairwise(sorted(diff)):
            for item in diff[y][0]:
                sections[item] += 1
            for item in diff[y][1]:
                sections[item] -= 1
                if sections[item] == 0:
                    del sections[item]
            width = gettotallength(sections)
            s = width * (y1 - y)
            areas[(y, y1, width)] = s
        # print(areas)
        totalarea = sum(areas.values())
        target = totalarea / 2
        curarea = 0
        for key in areas.keys():
            if curarea + areas[key] >= target:
                needed = target - curarea
                h1 = needed / key[2]
                return key[0] + h1
            curarea += areas[key]
