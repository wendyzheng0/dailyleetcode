###
# 假设你有一个特殊的键盘包含下面的按键：
# A：在屏幕上打印一个 'A'。
# Ctrl-A：选中整个屏幕。
# Ctrl-C：复制选中区域到缓冲区。
# Ctrl-V：将缓冲区内容输出到上次输入的结束位置，并显示在屏幕上。
# 现在，你可以 最多 按键 n 次（使用上述四种按键），返回屏幕上最多可以显示 'A' 的个数 。
#
# 如果最后用了Ctrl-V，那肯定是最后几个都是Ctrl-V，而且前面是Ctrl-A，Ctrl-C，否则这样的组合可以获得更多的A
# 然后用动态规划解答
class Solution:
    def maxA(self, n: int) -> int:
        # f[i]: longest length can get when press i times.
        # 1. f[i-1]+1, press A in ith
        # 2. max(f[j]*(i-j-1), 0<j<i-2), press Ctrl-V in ith, Ctrl-A in j+1th, Ctrl-C in j+2th
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + 1
            for j in range(i - 2):
                f[i] = max(f[i], f[j] * (i - j - 1))
        # print(f)
        return f[n]
