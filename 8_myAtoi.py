import re


###
# 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数。
# 函数 myAtoi(string s) 的算法如下：
# 空格：读入字符串并丢弃无用的前导空格（" "）
# 符号：检查下一个字符（假设还未到字符末尾）为 '-' 还是 '+'。如果两者都不存在，则假定结果为正。
# 转换：通过跳过前置零来读取该整数，直到遇到非数字字符或到达字符串的结尾。如果没有读取数字，则结果为0。
# 舍入：如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被舍入为 −231 ，大于 231 − 1 的整数应该被舍入为 231 − 1 。
# 返回整数作为最终结果。
#
# 直接按要求组合起来最快，正则表达式反而慢了。
class Solution:
    def myAtoi1(self, s: str) -> int:
        INT_MAX, INT_MIN = (1 << 31) - 1, -(1 << 31)
        m = re.match(' *([+-]?)(0*)([0-9]*)', s)
        res = int(m.group(3)) if m.group(3) != '' else 0
        if m.group(1) == '-':
            return max(-res, INT_MIN)
        else:
            return min(res, INT_MAX)

    def myAtoi(self, s: str) -> int:
        start = 0
        while start < len(s) and s[start] == ' ':
            start += 1
        res = 0
        if start >= len(s):
            return 0
        possitive = True
        if s[start] == '-':
            possitive = False
            start += 1
        elif s[start] == '+':
            start += 1
        while start < len(s) and '0' == s[start]:
            start += 1
        INT_MAX, INT_MIN, ABS_MAX = (1 << 31) - 1, -(1 << 31), 1 << 31
        while start < len(s) and '0' <= s[start] <= '9' and res <= ABS_MAX:
            res = res * 10 + int(s[start])
            start += 1
        # print(f"res:{res}, INT_MAX:{INT_MAX}, INT_MIN:{INT_MIN}, ABS_MAX:{ABS_MAX}")
        if possitive:
            return res if res <= INT_MAX else INT_MAX
        else:
            return -res if res <= ABS_MAX else INT_MIN
