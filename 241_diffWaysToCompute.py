from typing import List


###
# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。
# 生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。
#
# 每遇到一个运算符就把式子分成两部分，分别计算左右两边的结果，然后组合起来。
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def cal(left, right):
            res = []
            for i in range(left, right):
                op = expression[i]
                if op in '+-*':
                    op = expression[i]
                    leftres = cal(left, i)
                    rightres = cal(i + 1, right)
                    for lres in leftres:
                        for rres in rightres:
                            if op == '+':
                                res.append(lres + rres)
                            elif op == '-':
                                res.append(lres - rres)
                            elif op == '*':
                                res.append(lres * rres)
            if len(res) == 0:
                # print(f"{left}, {right}, {expression[left:right]}")
                return [int(expression[left:right])]
            return res
        return cal(0, len(expression))
