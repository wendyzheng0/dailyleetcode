###
# 给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 对于有n个元素的排列，如果第一个元素确定了，后面就有(n-1)!种排列。所以可以先计算出(n-1)!，然后根据k除以(n-1)!的商来确定第一个元素，然后根据余数来确定后面的元素。
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        cnt = []
        p = 1
        for i in range(1, n):
            p *= i
            cnt.append(p)
        s = []
        cand = [v for v in range(1, n + 1)]
        k -= 1
        for i in range(n - 2, -1, -1):
            pos = k // cnt[i]
            # print(f"k:{k}, cnt[{i}]:{cnt[i]}, pos:{pos}, cand:{cand}")
            s.append(cand[pos])
            del cand[pos]
            k = k % cnt[i]
        s.append(cand[0])
        # print(s)
        return ''.join(str(v) for v in s)
