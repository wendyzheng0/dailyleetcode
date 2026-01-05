from typing import List, Optional


###
# 给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。
#
# 递归生成所有可能的二叉搜索树。本来怕两个数共享子树会有问题，其实如果只读是没有问题的，但如果要求存储分开的话需要deepcopy。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start, end):
            if start > end:
                return [None]
            res = []
            for r in range(start, end + 1):
                leftroots = generate(start, r - 1)
                rightroots = generate(r + 1, end)
                if leftroots and rightroots:
                    for lr in leftroots:
                        for rr in rightroots:
                            root = TreeNode(r)
                            root.left = lr
                            root.right = rr
                            res.append(root)
            return res
        return generate(1, n)
