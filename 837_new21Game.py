###
# 爱丽丝参与一个大致基于纸牌游戏 “21点” 规则的游戏，描述如下：
# 爱丽丝以 0 分开始，并在她的得分少于 k 分时抽取数字。 抽取时，她从 [1, maxPts] 的范围中随机获得一个整数作为分数进行累计，其中 maxPts 是一个整数。 每次抽取都是独立的，其结果具有相同的概率。
# 当爱丽丝获得 k 分 或更多分 时，她就停止抽取数字。
# 爱丽丝的分数不超过 n 的概率是多少？
# 与实际答案误差不超过 10-5 的答案将被视为正确答案。
#
# 开始的时候列举了获得各种分数的组合数然后求概率，后来发现各种组合出现的概率不是一样的，不能那样算。后来改成用动态规划，从后往前推。
# 因为分数是k到n的时候概率是1，大于n小于k+MaxPts-1的时候概率是0，所以可以推导出当分数是k-1的时候的赢的概率是多少。再依次往前推导直到0.
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # p[i]: possibility to win when gets i points
        p = [0] * (k + maxPts)
        for i in range(k, min(n + 1, k + maxPts)):
            p[i] = 1
        p[k - 1] = min(n - k + 1, maxPts) / maxPts
        for i in range(k - 2, -1, -1):
            p[i] = p[i + 1] - (p[i + maxPts + 1] - p[i + 1]) / maxPts
        return p[0]