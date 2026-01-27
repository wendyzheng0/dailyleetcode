###
# 给定链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
# 用归并排序解决。之前还尝试快排，根据head把链表分为小于head和大于head的两部份，结果操作太多超时了。
# 还是归并排序好一点。后来发现把值写到数组排序后再赋值回去竟然更快。我本来写了一个用数组保存指针然后
# 按照val排序，再重构链表的方法竟然超内存。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        dummy = ListNode(next=head)
        slow, fast = dummy, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None
        head = self.sortList(head)
        head2 = self.sortList(head2)
        p = dummy
        while head and head2:
            if head.val < head2.val:
                p.next = head
                p, head = p.next, head.next
            else:
                p.next = head2
                p, head2 = p.next, head2.next
        if head:
            p.next = head
        if head2:
            p.next = head2
        return dummy.next

    def sortList1(self, head: ListNode) -> ListNode:
        arr = []
        p = head
        while p:
            arr.append(p.val)
            p = p.next
        # arr.sort(key=lambda x: x.val)
        arr.sort()
        p = head
        for v in arr:
            p.val = v
            p = p.next
        return head
