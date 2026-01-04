from typing import List
from math import isqrt


###
# 给你一个整数数组 nums，请你返回该数组中恰有四个因数的这些整数的各因数之和。如果数组中不存在满足题意的整数，则返回 0 。
#
# 用比较直观的方法做的，速度不是很快。数学方法比较快，但不太明白。
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            f = 2
            cnt = 2
            s = 1 + num
            t = []
            while f <= isqrt(num):
                if num % f == 0:
                    if f == num // f:
                        cnt += 1
                        t.append(f)
                    else:
                        cnt += 2
                        t.append(f)
                        t.append(num // f)
                    s += f + num // f
                    if cnt > 4:
                        break
                f += 1
            if cnt == 4:
                print(f"num:{num}, s:{s}, cnt:{cnt}, t:{t}")
                res += s
        return res
