###
# 给定方法 rand7 可生成 [1,7] 范围内的均匀随机整数，试写一个方法 rand10 生成 [1,10] 范围内的均匀随机整数。
# 你只能调用 rand7() 且不能调用其他方法。请不要使用系统的 Math.random() 方法。
# 每个测试用例将有一个内部参数 n，即你实现的函数 rand10() 在测试时将被调用的次数。请注意，这不是传递给 rand10() 的参数。
#
# 把rand10分成两次求，第一次求出是1-5还是6-10，第二次在1-5或6-10中选一个，这样概率是相等的。

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        first = rand7()
        while first > 6:
            first = rand7()
        second = rand7()
        while second > 5:
            second = rand7()
        return second if (first & 1) == 1 else second + 5
