from typing import List


###
# 给你一个整数 n，表示公司中员工的数量。每位员工都分配了一个从 1 到 n 的唯一 ID ，其中员工 1 是 CEO。另给你两个下标从 1 开始的整数数组 present 和 future，两个数组的长度均为 n，具体定义如下：
# present[i] 表示第 i 位员工今天可以购买股票的 当前价格 。
# future[i] 表示第 i 位员工明天可以卖出股票的 预期价格 。
# 公司的层级关系由二维整数数组 hierarchy 表示，其中 hierarchy[i] = [ui, vi] 表示员工 ui 是员工 vi 的直属上司。
# 此外，再给你一个整数 budget，表示可用于投资的总预算。
# 公司有一项折扣政策：如果某位员工的直属上司购买了公司的股票，那么该员工可以以 半价 购买股票（即 floor(present[v] / 2)）。
# 请返回在不超过给定预算的情况下可以获得的 最大利润 。
# 注意：
# 每只股票最多只能购买一次。
# 不能使用股票未来的收益来增加投资预算，购买只能依赖于 budget。
#
# 动态规划和递推结合。关键是dfs返回的结构比较复杂，描述了子树在各种budget下面父节点购买或不购买股票时的最大利润。
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for u, v in hierarchy:
            g[u - 1].append(v - 1)

        def dfs(node):
            # subF[j][0/1], max subtree profit when budget <= j and buy/not buy node
            subF = [[0, 0] for _ in range(budget + 1)]
            for c in g[node]:
                fy = dfs(c) # fy[j][0] not buying node c, fy[j][1] buying node c
                for j in range(budget, -1, -1):
                    for jy in range(j + 1):
                        subF[j][0] = max(subF[j][0], subF[j - jy][0] + fy[jy][0])
                        subF[j][1] = max(subF[j][1], subF[j - jy][1] + fy[jy][1])
            f = [[0, 0] for _ in range(budget + 1)]
            for j in range(budget, -1, -1):
                for k in range(2):
                    cost = present[node] // (k + 1)
                    if j >= cost:
                        f[j][k] = max(subF[j][0], subF[j - cost][1] + future[node] - cost)
                    else:
                        f[j][k] = subF[j][0]
            return f
        return dfs(0)[budget][0]
