from functools import cache

###
# 97. Interleaving String
# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| <= 1
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 注意：a + b 意味着字符串 a 和 b 连接。
class Solution:
    ###
    # 用动态规划，也就是递归+记忆化搜索。
    # dfs(idx1, idx2) 的意义是，s1[0..idx1]和s2[0..idx2]能否交错组成s3[0..idx1+idx2+1]。
    # 终止条件是idx1和idx2都小于0，说明s1和s2都被用完了，返回True。
    # 否则，如果s1的当前字符和s3的当前字符相等，并且去掉这个字符后s1和s2能交错组成去掉这个字符后的s3，
    # 那么说明s1和s2能交错组成s3，返回True。
    # 对于s2同理。
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        @cache
        def dfs(idx1, idx2):
            if idx1 < 0 and idx2 < 0:
                return True
            if idx1 >= 0 and s1[idx1] == s3[idx1 + idx2 + 1] and dfs(idx1 - 1, idx2):
                return True
            if idx2 >= 0 and s2[idx2] == s3[idx1 + idx2 + 1] and dfs(idx1, idx2 - 1):
                return True
            return False

        return ((len1 + len2) == len3) and dfs(len1 - 1, len2 - 1)

    ###
    # 把上面动态规划的方法改成递推的实现。f[i][j]表示s1[0..i-1]和s2[0..j-1]能否交错组成s3[0..i+j-1]。
    # 初始条件是f[0][0] = True，第一行和第一列的值比较特殊，先计算出来。
    # 最终答案是f[len1][len2]
    # 这个方法和上面的动态规划速度和内存消耗差不多。
    def isInterleave_2(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)
        if (len1 + len2) != len3:
            return False
        f = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        f[0][0] = True
        for i in range(len2):
            f[0][i + 1] = f[0][i] and s2[i] == s3[i]
        for i in range(len1):
            f[i + 1][0] = f[i][0] and s1[i] == s3[i]
            for j in range(len2):
                f[i + 1][j + 1] = (f[i][j + 1] and s1[i] == s3[i + j + 1]) or \
                                  (f[i + 1][j] and s2[j] == s3[i + j + 1])
        return f[len1][len2]
    
    ###
    # 笨办法
    # dfs(s1, s2, s3) 的意义是，当s1和s3有共同前缀时，s3是否可以由s1和s2交错组成。
    # 枚举每种可能的分割方式，检查是否有一种方式可以成功。这个方法排名几乎垫底。
    # 后来改成用index也没有好很多，只是节省了点内存。
    def isInterleave_1(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def dfs(s1, s2, s3):
            # print(f"s1:{s1}, s2:{s2}, s3:{s3}")
            len1, len2, len3 = len(s1), len(s2), len(s3)
            n = min(len1, len3)
            if s2 == '':
                return s1 == s3
            for i in range(n):
                if s1[i] == s3[i]:
                    if i + 1 < len3 and s2[0] == s3[i + 1]:
                        res = dfs(s2, s1[i + 1:], s3[i + 1:])
                        if res:
                            return True
                else:
                    break
            return False
        return dfs(s1, s2, s3) or dfs(s2, s1, s3)