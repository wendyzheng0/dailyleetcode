from typing import Optional


###
# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。如果有多种构造方法，请你返回任意一种。
# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
#
# 先按顺序遍历二叉搜索树，把节点都放到数组里，然后从数组重新构建平衡二叉搜索树。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        allnodes = []

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            allnodes.append(node)
            dfs(node.right)
        dfs(root)

        def genTree(left, right):
            if left == right:
                return None
            m = (left + right) // 2
            allnodes[m].left = genTree(left, m)
            allnodes[m].right = genTree(m + 1, right)
            return allnodes[m]

        return genTree(0, len(allnodes))
