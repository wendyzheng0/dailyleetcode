from typing import List


###
# 给定一个整数数组 weights 和两个整数 w1 和 w2 表示两个袋子的 最大 容量。
# 每个物品 最多 可以放入一个袋子中，使得：
# 袋子 1 最多 总共可以装 w1 重量。
# 袋子 2 最多 总共可以装 w2 重量。
# 返回两个袋子可以装入的 最大 总重量。
#
# 比普通背包多了1维，想着用set可能快点（maxWeight1），结果后来发现还是二维数组更快（maxWeight）。
class Solution:
    def maxWeight(self, weights: List[int], w1: int, w2: int) -> int:
        f = [[False] * (w2 + 1) for _ in range(w1 + 1)]
        f[0][0] = True
        res = 0
        for i in range(len(weights)):
            for j in range(w1, -1, -1):
                for k in range(w2, -1, -1):
                    if f[j][k] and j + weights[i] <= w1:
                        f[j + weights[i]][k] = True
                        # print(f"({j}, {k}) -> ({j+weights[i]}, {k})")
                    if f[j][k] and k + weights[i] <= w2:
                        f[j][k + weights[i]] = True
                        # print(f"({j}, {k}) -> ({j}, {k+weights[i]})")
        for j in range(w1 + 1):
            for k in range(w2 + 1):
                if f[j][k]:
                    # print(f"{j}, {k}")
                    res = max(res, j + k)
        return res

    def maxWeight1(self, weights: List[int], w1: int, w2: int) -> int:
        n = len(weights)
        f = set({(0, 0)})
        res = 0
        for i in range(n):
            for item in f.copy():
                if item[0] + weights[i] <= w1:
                    f.add((item[0] + weights[i], item[1]))
                    res = max(res, item[0] + item[1] + weights[i])
                if item[1] + weights[i] <= w2:
                    f.add((item[0], item[1] + weights[i]))
                    res = max(res, item[0] + item[1] + weights[i])
            # print(f)
        return res
