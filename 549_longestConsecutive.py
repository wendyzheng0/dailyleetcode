from typing import Optional


###
# 给定二叉树的根 root ，返回树中最长连续路径的长度。
# 连续路径是路径中相邻节点的值相差 1 的路径。此路径可以是增加或减少。
# 例如， [1,2,3,4] 和 [4,3,2,1] 都被认为有效，但路径 [1,2,4,3] 无效。
# 另一方面，路径可以是子-父-子顺序，不一定是父子顺序。
#
# 递归检查每个节点结束的递增递减最长路径长度。递归过程中更新最长路径长度。
# 由于最长递增和最长递减路径都是以当前节点为路径，所以二者和减一就是经过当前节点路径的最长连续路径长度。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            if node is None:
                return [0, 0]
            nonlocal res
            p1 = p2 = 1
            if node.left:
                left = dfs(node.left)
                if node.left.val + 1 == node.val:
                    p1 = max(p1, left[0] + 1)
                elif node.left.val == node.val + 1:
                    p2 = max(p2, left[1] + 1)
            if node.right:
                right = dfs(node.right)
                if node.right.val + 1 == node.val:
                    p1 = max(p1, right[0] + 1)
                elif node.right.val == node.val + 1:
                    p2 = max(p2, right[1] + 1)
            # print(f"node:{node.val}, p1:{p1}, p2:{p2}")
            res = max(res, p1 + p2 - 1)
            return [p1, p2]
        dfs(root)
        return res
