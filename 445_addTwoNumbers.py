from typing import Optional


###
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 利用递归实现。后来发现别人把链表转成数组更快。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getLen(node: ListNode) -> int:
            cnt = 0
            while node is not None:
                cnt += 1
                node = node.next
            return cnt

        def addNum(idx1: int, node1: ListNode, idx2: int, node2: ListNode) -> ListNode:
            nxnode = None
            if idx1 > idx2:
                nxnode = addNum(idx1 - 1, node1.next, idx2, node2)
                val = node1.val
            elif idx1 < idx2:
                nxnode = addNum(idx1, node1, idx2 - 1, node2.next)
                val = node2.val
            else:
                if idx1 > 1:
                    nxnode = addNum(idx1 - 1, node1.next, idx2 - 1, node2.next)
                val = node1.val + node2.val
            if nxnode is not None and nxnode.val >= 10:
                val += nxnode.val // 10
                nxnode.val = nxnode.val % 10
            newnode = ListNode(val, nxnode)
            return newnode

        len1 = getLen(l1)
        len2 = getLen(l2)
        sumnode = addNum(len1, l1, len2, l2)
        if sumnode.val >= 10:
            temp = ListNode(sumnode.val // 10, sumnode)
            sumnode.val = sumnode.val % 10
            sumnode = temp
        return sumnode
