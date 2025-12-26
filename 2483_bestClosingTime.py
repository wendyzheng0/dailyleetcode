###
# 给你一个顾客访问商店的日志，用一个下标从 0 开始且只包含字符 'N' 和 'Y' 的字符串 customers 表示：
# 如果第 i 个字符是 'Y' ，它表示第 i 小时有顾客到达。
# 如果第 i 个字符是 'N' ，它表示第 i 小时没有顾客到达。
# 如果商店在第 j 小时关门（0 <= j <= n），代价按如下方式计算：
# 在开门期间，如果某一个小时没有顾客到达，代价增加 1 。
# 在关门期间，如果某一个小时有顾客到达，代价增加 1 。
# 请你返回在确保代价 最小 的前提下，商店的 最早 关门时间。
# 注意，商店在第 j 小时关门表示在第 j 小时以及之后商店处于关门状态。
#
# 先计算不关门的成本，然后从后往前遍历计算时间j关门的成本，记录最小成本和对应的时间。
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cost = mincost = customers.count('N')
        res = len(customers)
        for j in range(len(customers) - 1, -1, -1):
            if customers[j] == 'Y':
                cost += 1
            else:
                cost -= 1
                if mincost >= cost:
                    mincost = cost
                    res = j
        return res
