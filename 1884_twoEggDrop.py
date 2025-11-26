from functools import cache


###
# 给你 2 枚相同 的鸡蛋，和一栋从第 1 层到第 n 层共有 n 层楼的建筑。
# 已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都 会碎 ，从 f 楼层或比它低 的楼层落下的鸡蛋都 不会碎 。
# 每次操作，你可以取一枚 没有碎 的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 重复使用 这枚鸡蛋。
# 请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
# 用动态规划求解。对于n层楼，尝试从1..n层扔第一个鸡蛋，如果在第i层扔碎了，那至多需要i次操作确定f的值。
# 如果没碎，那相当于把问题规模缩小到了n-i层楼。
# 用数学的方法更简单，ceil((sqrt(n * 8 + 1) - 1) / 2)。详细解答看灵神的题解。
class Solution:
    def twoEggDrop1(self, n: int) -> int:
        f = [0] * (n + 1)
        f[1] = 1
        for m in range(2, n + 1):
            f[m] = min(max(f[m - i] + 1, i) for i in range(1, m + 1))
            # print(f"{m}:{f[m]}")
        return f[n]

    def twoEggDrop(self, n: int) -> int:
        # dfs(n) = if drop from floor i and broken, need i times
        #          if not broken, need dfs(n-i)+1times
        # dfs(n) = min(max(dfs(n-i)+1, i) for i in range(1, n+1))
        # dfs(1) = 1
        @cache
        def dfs(n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            res = min(max(dfs(n - i) + 1, i) for i in range(1, n + 1))
            # print(f"n:{n},res:{res}")
            return res
        return dfs(n)
