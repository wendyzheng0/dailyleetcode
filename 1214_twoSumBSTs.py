from typing import Optional


###
# 给出两棵二叉搜索树的根节点 root1 和 root2 ，请你从两棵树中各找出一个节点，使得这两个节点的值之和等于目标值 Target。
# 如果可以找到返回 True，否则返回 False。
#
# 这题比较直观，先遍历root1得到所有节点值，然后遍历root2，检查每个点是否可以和root1的点组成target。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        numset = set()

        def dfs(parent):
            numset.add(parent.val)
            if parent.left:
                dfs(parent.left)
            if parent.right:
                dfs(parent.right)

        def searchdfs(parent):
            if target - parent.val in numset:
                return True
            if parent.left and searchdfs(parent.left):
                return True
            if parent.right and searchdfs(parent.right):
                return True
            return False

        dfs(root1)
        return searchdfs(root2)
