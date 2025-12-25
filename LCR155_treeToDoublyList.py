from typing import Optional


###
# 将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。
# 对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
# 特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。
#
# 这题比较直观，中序遍历搜索树，每次遍历的时候更新根节点的指向，返回转换后的头尾节点
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(node):
            left = right = node
            if node.left:
                left, tmp = dfs(node.left)
                node.left = tmp
                tmp.right = node
            if node.right:
                tmp, right = dfs(node.right)
                node.right = tmp
                tmp.left = node
            return [left, right]

        if root is None:
            return None
        head, tail = dfs(root)
        head.left = tail
        tail.right = head
        return head
