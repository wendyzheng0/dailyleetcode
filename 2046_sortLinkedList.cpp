/**
给你一个链表的头结点 head ，这个链表是根据结点的绝对值进行升序排序, 返回重新根据节点的值进行升序排序的链表。

遍历链表，遇到负数放到表头。
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
 class Solution {
    public:
        ListNode* sortLinkedList(ListNode* head) {
            ListNode *pre = head, *p = pre->next;
            while (p != NULL) {
                if (p->val < 0) {
                    pre->next = p->next;
                    p->next = head;
                    head = p;
                    p = pre->next;
                } else {
                    pre = p;
                    p = p->next;
                }
            }
            return head;
        }
    };