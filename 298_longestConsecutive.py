from typing import Optional


###
# 给你一棵指定的二叉树的根节点 root ，请你计算其中 最长连续序列路径 的长度。
# 最长连续序列路径 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 - 子」关系连接而产生的任意路径。且必须从父节点到子节点，反过来是不可以的。
#
# 递归检查每个节点开始的最长连续序列路径长度。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def checkNode(node, length):
            ret = length
            if node.left:
                if node.val + 1 == node.left.val:
                    ret = max(ret, checkNode(node.left, length + 1))
                else:
                    ret = max(ret, checkNode(node.left, 1))
            if node.right:
                if node.val + 1 == node.right.val:
                    ret = max(ret, checkNode(node.right, length + 1))
                else:
                    ret = max(ret, checkNode(node.right, 1))
            return ret
        return checkNode(root, 1)
