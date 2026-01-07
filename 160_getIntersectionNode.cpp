#include <unordered_set>

/**
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
今天参加了一个面试做的c++的题，竟然把问题想复杂了，其实很简单的方法。先遍历两个链表得到长度，然后让长的链表先走长度差步，然后两个链表一起走，直到找到相交节点。
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 class Solution {
    public:
        ListNode *getIntersectionNode1(ListNode *headA, ListNode *headB) {
            ListNode *node = headA;
            int lenA = 0;
            int lenB = 0;
            while (node) {
                node = node->next;
                lenA++;
            }
            node = headB;
            while (node) {
                node = node->next;
                lenB++;
            }
            ListNode *pa = headA, *pb = headB;
            if (lenA > lenB) {
                for (int i = 0; i < lenA - lenB; i++) {
                    pa = pa->next;
                }
            } else {
                for (int i = 0; i < lenB - lenA; i++) {
                    pb = pb->next;
                }
            }
            while (pa != pb && pa != NULL && pb != NULL) {
                pa = pa->next;
                pb = pb->next;
            }
            if (pa == pb) {
                return pa;
            } else {
                return NULL;
            }
        }
        ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
            unordered_set<ListNode*> nodeset;
            ListNode *node = headA;
            while (node) {
                nodeset.insert(node);
                node = node->next;
            }
            
            node = headB;
            while (node) {
                if (nodeset.contains(node)) {
                    return node;
                }
                node = node->next;
            }
            return node;
        }
    };