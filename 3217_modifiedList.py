from typing import List, Optional


###
# 给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        occur = set(nums)
        pre = dummyhead = ListNode(next=head)
        cur = head
        while cur is not None:
            if cur.val not in occur:
                pre.next = cur
                pre = cur
            cur = cur.next
        pre.next = None
        return dummyhead.next

