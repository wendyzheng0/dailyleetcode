from collections import Counter


###
# 如果整数  x 满足：对于每个数位 d ，这个数位 恰好 在 x 中出现 d 次。那么整数 x 就是一个 数值平衡数 。
# 给你一个整数 n ，请你返回 严格大于 n 的 最小数值平衡数 。
#
# 暴力法，因为总有一个数可以满足条件，所以从n开始，每次加1，检查是否是数值平衡数。
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            cnt = Counter(str(n))
            if all(int(v) == c for v, c in cnt.items()):
                return n