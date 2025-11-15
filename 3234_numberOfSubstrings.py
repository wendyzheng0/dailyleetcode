###
# 给你一个二进制字符串 s。
# 请你统计并返回其中 1 显著 的 子字符串 的数量。
# 如果字符串中 1 的数量 大于或等于 0 的数量的 平方，则认为该字符串是一个 1 显著 的字符串 。
#
# 直接算会超时，看了题解利用连续1的特性通过枚举0加速计算。
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [-1]
        total1 = 0
        res = 0
        for r in range(n):
            if s[r] == '0':
                zeros.append(r)
            else:
                total1 += 1
                # [zeros[-1] + 1,r] only contains '1'
                res += r - zeros[-1]
            # print(f"r:{r}, {s[:r+1]}, res:{res}")
            for idx in range(len(zeros) - 1, 0, -1):
                # num of '0' in [q,r]
                z = len(zeros) - idx
                if z * z > total1:
                    break
                p, q = zeros[idx - 1], zeros[idx]
                # num of '1' in [q,r]
                ones = r - q + 1 - z
                # [p+1,q-1] only contains '1', if [q,r] is valid, [p+1,r]... [q,r] are valid, otherwise [p+1,r]... [q-z*z-ones, r] are valid
                res += max(q - max(z * z - ones, 0) - p, 0)
                # print(f"p:{p},q:{q},{s[p+1:q+1]},one:{ones},z:{z},res:{res}")
                z += 1
        return res
