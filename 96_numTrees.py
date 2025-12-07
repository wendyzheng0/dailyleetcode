###
# 给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
#
# 由于二叉搜索树的种数只和节点数有关，和具体节点的值无关，所以可以用dp[x]表示有x个节点的时候二叉搜索树的种数。
# 用动态规划的方法，对于x个节点，尝试以任意一个节点为根，剩余左边节点组为左子树，右边为右子树，所能组成的二叉搜索树
# 种数为二者的乘积。
class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i][j]: n[i:j+1]的搜索树数量
        # dp[i][j] = sigma(dp[i][k-1] * dp[k+1][j]) k=i..j
        # 当j-i相等时，搜索树的数量是一样的，只和节点个数有关。于是变为
        # dp[x] = sigma(dp[y] * dp[x-y-1]) y=0..x-1, dp[0] = dp[1] = 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for x in range(2, n + 1):
            for y in range(x):
                dp[x] += dp[y] * dp[x - y - 1]
        return dp[n]
