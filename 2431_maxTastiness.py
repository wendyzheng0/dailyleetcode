from typing import List
from functools import cache

###
# 你有两个非负整数数组 price 和 tastiness，两个数组的长度都是 n。同时给你两个非负整数 maxAmount 和 maxCoupons。
# 对于范围 [0, n - 1] 中的每一个整数 i:
# price[i] 描述了第 i 个水果的价格。
# tastiness[i] 描述了第 i 个水果的味道。
# 你想购买一些水果，这样总的味道是最大的，总价不超过 maxAmount。
# 此外，你还可以用优惠券以 半价 购买水果 (向下取整到最接近的整数)。您最多可以使用 maxCoupons 次该优惠券。
# 返回可购买的最大总口味。
# 注意:
# 每个水果最多只能购买一次。
# 一个水果你最多只能用一次折价券。
#
# 用了dfs+cache来解。
class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        @cache
        def dfs(i, amount, coupons):
            if i < 0 or amount < 0:
                return 0
            p0 = p1 = p2 = dfs(i - 1, amount, coupons)
            if amount >= price[i]:
                p1 = dfs(i - 1, amount - price[i], coupons) + tastiness[i]
            if amount >= price[i] // 2 and coupons > 0:
                p2 = dfs(i - 1, amount - price[i] // 2, coupons - 1) + tastiness[i]
            return max(p0, p1, p2)
        return dfs(len(price) - 1, maxAmount, maxCoupons)
