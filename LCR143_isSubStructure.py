from typing import Optional


###
# 给定两棵二叉树 tree1 和 tree2，判断 tree2 是否以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
# 注意，空树 不会是以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
#
# 遍历A寻找值为B的根节点的节点，然后判断以该节点为根的子树是否与B相同。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        def isACoverB(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if a is None:
                return b is None
            elif b is None:
                return True
            if a.val != b.val:
                return False
            return isACoverB(a.left, b.left) and isACoverB(a.right, b.right)

        def iteratetree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if b is None or a is None:
                return False
            if a.val == b.val and isACoverB(a, b):
                return True
            if iteratetree(a.left, b) or iteratetree(a.right, b):
                return True
            return False

        return iteratetree(A, B)
