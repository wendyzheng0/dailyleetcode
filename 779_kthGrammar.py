###
# 我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。
# 例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
# 给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）
#
# 一个数字会被转换为两个数字，所以第i行有2**(i-1)个数字，第i行的第j个数字由第i-1行的j//2的数字决定，是转换后的第一个还是第二个数字
# 则可以根据j是奇数还是偶数决定，一直推到第一行就可以知道第n行的第k个数字是怎么转换过来的再据此转换一下就可以了。
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        idxs = []
        i = k - 1
        for j in range(n - 1):
            idxs.append(i % 2)
            i = i // 2
        v = 0
        conv = {0: [0, 1], 1: [1, 0]}
        # print(f"idxs: {idxs}")
        for i in range(len(idxs) - 1, -1, -1):
            v = conv[v][idxs[i]]
            # print(v)
        return v
