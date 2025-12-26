###
# 面试题 16.26. 计算器
# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
# 表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 开始的时候用栈记录遍历过的数字和符号，如果栈顶是乘除，则先计算栈顶和当前数字，然后更新栈顶，再把符号入栈。
# 后来发现这样慢了，可以优化成遇到新符号的时候就计算前一个符号，如果前一个符号是加减，直接把当前数字变正负号后入栈，如果是乘除，则用栈顶成员和当前数字计算结果就可以了。
# 后来进一步简化，用变量prevalue记录栈顶数字，遇到加减，把prevalue加到结果种，根据前一个符号更新prevalue为当前数字。遇到乘除，用prevalue和当前数字运算。最后结果是res+prevalue。
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        prevalue = 0
        presign = '+'
        value = 0
        for c in s + '+':
            if '0' <= c <= '9':
                value = value * 10 + int(c)
            elif c in '+-*/':
                if presign == '+':
                    res += prevalue
                    prevalue = value
                elif presign == '-':
                    res += prevalue
                    prevalue = -value
                elif presign == '*':
                    prevalue *= value
                elif presign == '/':
                    prevalue = int(prevalue / value)
                value = 0
                presign = c
        return res + prevalue

    def calculate1(self, s: str) -> int:
        stack = []
        value = 0
        computelevel = {'+': 1, '-': 1, '*': 2, '/': 2}

        def cal(v1, op, v2):
            if op == '+':
                return v1 + v2
            elif op == '-':
                return v1 - v2
            elif op == '*':
                return v1 * v2
            else:
                return v1 // v2

        for c in s + '+0':
            if c == ' ':
                continue
            if '0' <= c <= '9':
                value = value * 10 + int(c)
            else:
                if stack and computelevel[stack[-1]] == 2:
                    op = stack[-1]
                    v1 = stack[-2]
                    del stack[-1]
                    del stack[-1]
                    stack.append(cal(v1, op, value))
                    stack.append(c)
                else:
                    stack.append(value)
                    stack.append(c)
                value = 0
                # print(stack)
        stack.append(value)
        res = stack[0]
        for i in range(1, len(stack), 2):
            res = cal(res, stack[i], stack[i + 1])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.calculate("3+2*2")) # 7
    print(solution.calculate(" 3/2 ")) # 1
    print(solution.calculate(" 3+5 / 2 ")) # 5
    print(solution.calculate("282-1*2*13-30-2*2*2/2-95/5*2+55+804+3024")) # 4067
    print(solution.calculate("14-3/2")) # 13
