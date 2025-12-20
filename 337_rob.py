from typing import Optional


###
# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
# 除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
# 给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
#
# 分别统计当前节点偷和不偷的时候子树的偷和不偷的最大效益，组合成当前子树的偷和不偷根结点的最大效益。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            left = [0, 0]
            right = [0, 0]
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            notsel = max(left) + max(right)
            sel = left[0] + right[0] + node.val
            return [notsel, sel]
        return max(dfs(root))
