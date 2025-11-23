from typing import Optional, List
from collections import defaultdict


###
# 给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。
# 一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
#
# 递归计算每个节点的子树元素和，然后统计出现次数最多的子树元素和。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnt = defaultdict(int)
        mx = 0

        def check(parent):
            nonlocal mx
            if parent is None:
                return
            s = parent.val
            if parent.left is not None:
                s += check(parent.left)
            if parent.right is not None:
                s += check(parent.right)
            cnt[s] += 1
            mx = max(mx, cnt[s])
            return s

        check(root)
        # print(cnt)
        res = []
        for k, v in cnt.items():
            if v == mx:
                res.append(k)
        return res
