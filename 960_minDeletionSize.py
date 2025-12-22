from typing import List


###
# 给定由 n 个小写字母字符串组成的数组 strs ，其中每个字符串长度相等。
# 选取一个删除索引序列，对于 strs 中的每个字符串，删除对应每个索引处的字符。
# 比如，有 strs = ["abcdef","uvwxyz"] ，删除索引序列 {0, 2, 3} ，删除后为 ["bef", "vyz"] 。
# 假设，我们选择了一组删除索引 answer ，那么在执行删除操作之后，最终得到的数组的行中的 每个元素 都是按字典序排列的（即 (strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1]) 和 (strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1]) ，依此类推）。
# 请返回 answer.length 的最小可能值 。
#
# 动态规划。记录以第i列结尾的子序列的最大长度，然后遍历之前的每一列，如果当前列的字符比之前的某一列的字符都大，则更新最大长度。
# 最后返回m - keep，其中keep是最大的以某一列结尾的子序列的长度。
# 之前尝试用最长递增子序列的方法优化，结果发现没法优化。当只有一行的时候，长度为i的最长子序列的最小末尾是递增的，可以用二分法快速找到长度为i的子序列的最小末尾。
# 但是多行的时候他们之间就没有这种关系了。f的意义是当前列结尾的子序列的最大长度，而不是当前列结尾的子序列的最小末尾。
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs[0])
        f = []
        keep = 0
        for i in range(m):
            best = 0
            for j in range(i):
                if f[j] > best:
                    for v in strs:
                        if v[j] > v[i]:
                            break
                    else:
                        best = f[j]
            best += 1
            f.append(best)
            keep = max(keep, best)
        return m - keep
