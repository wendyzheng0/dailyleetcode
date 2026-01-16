from typing import Optional


###
# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
# L0 → L1 → … → Ln - 1 → Ln
# 请将其重新排列后变为：
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# 不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 用快慢指针遍历一遍找到中间节点，然后反转第二部分，最后合并两部分。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return
        slow = fast = head
        pre = None
        while fast is not None and fast.next is not None:
            fast = fast.next
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = None
        p = slow
        # revert second half
        pre = None
        while p is not None:
            nx = p.next
            p.next = pre
            pre = p
            p = nx
        second = pre
        # merge 2 list
        first = head
        while first is not None and second is not None:
            nxfisrt = first.next
            first.next = second
            nxsecond = second.next
            second.next = nxfisrt if nxfisrt is not None else nxsecond
            first = nxfisrt
            second = nxsecond
