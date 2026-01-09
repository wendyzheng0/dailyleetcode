from typing import Optional


###
# 给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。
# 返回包含原始树中所有 最深节点 的 最小子树 。
# 如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。
# 一个节点的 子树 是该节点加上它的所有后代的集合。
#
# 先求出树的深度，然后从根节点开始，如果当前节点的深度等于树的深度，则返回当前节点。
# 否则，递归求解左子树和右子树。如果左右子树都有最深节点，则返回当前节点。否则返回有最深节点的子树根节点。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def getdepth(node):
            if node is None:
                return 0
            return max(getdepth(node.left), getdepth(node.right)) + 1
        depth = getdepth(root)

        def getnode(node, level):
            if level == depth:
                return node
            leftnode = rightnode = None
            if node.left:
                leftnode = getnode(node.left, level + 1)
            if node.right:
                rightnode = getnode(node.right, level + 1)
            if leftnode and rightnode:
                return node
            if leftnode:
                return leftnode
            return rightnode
        return getnode(root, 1)
