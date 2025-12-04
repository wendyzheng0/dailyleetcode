from typing import Optional


# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 用一个数组记录遍历过的节点里面每一层的最左边节点。然后按照根-右节点-左节点的顺序遍历，每次遍历到
# 一个节点时，将该节点指向数组中该层的最左边节点，然后把自己更新为该层的最左边节点。
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        neighbor = [None] * 12

        def dfs(parent, layer):
            if parent is None:
                neighbor[layer] = None
                return
            parent.next = neighbor[layer]
            neighbor[layer] = parent
            if parent.right:
                dfs(parent.right, layer + 1)
            if parent.left:
                dfs(parent.left, layer + 1)
        dfs(root, 0)
        return root
