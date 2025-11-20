from typing import Optional


###
# 给你一棵二叉树的根节点 root ，返回树的 最大宽度 。
# 树的 最大宽度 是所有层中最大的 宽度 。
# 每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。
# 题目数据保证答案将会在  32 位 带符号整数范围内。
#
# 开始用递归做的widthOfBinaryTree1，提交能过，就是慢了点，写的也有点复杂。看到别人直接给每个节点标上全二叉树
# 的编号然后直接用编号计算宽度，代码简洁了很多。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = [(root, 1)]
        res = 0
        while que:
            width = que[-1][1] - que[0][1] + 1
            res = max(res, width)
            nextque = []
            for node, idx in que:
                if node.left:
                    nextque.append((node.left, idx * 2))
                if node.right:
                    nextque.append((node.right, idx * 2 + 1))
            que = nextque
        return res

    def widthOfBinaryTree1(self, root: Optional[TreeNode]) -> int:
        que = [root]
        res = 1
        def updateNumber(quearray, num):
            if quearray:
                if type(quearray[-1]) == int:
                    quearray[-1] += num
                else:
                    quearray.append(num)

        while que:
            nextque = []
            width = 0
            # print(que)
            for item in que:
                if type(item) == int:
                    updateNumber(nextque, item * 2)
                    continue
                if item.left is not None:
                    nextque.append(item.left)
                else:
                    updateNumber(nextque, 1)
                if item.right is not None:
                    nextque.append(item.right)
                else:
                    updateNumber(nextque, 1)
            while nextque and type(nextque[0]) == int:
                del nextque[0]
            while nextque and type(nextque[-1]) == int:
                del nextque[-1]
            # s = ''
            for item in nextque:
                # s = s + str(f"int:{item}" if type(item) == int else f"node:{item.val}") + ','
                width += item if type(item) == int else 1
            res = max(res, width)
            # print(s)
            # print(width)
            que = nextque
        return res
        