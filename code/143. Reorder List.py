#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :143. Reorder List.py
# @Time      :5/6/22
# @Author    :Eason Tang
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        def get_middle_node(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_linked_list(head):
            pre = None
            cur = head
            while cur:
                next_temp = cur.next
                cur.next = pre
                pre = cur
                cur = next_temp
            return pre

        def merge_list(l1, l2):
            while l1 and l2:
                l1_tmp = l1.next
                l2_tmp = l2.next

                l1.next = l2
                l1 = l1_tmp

                l2.next = l1
                l2 = l2_tmp

        mid = get_middle_node(head)
        l1 = head
        l2 = mid.next
        mid.next = None

        l2 = reverse_linked_list(l2)
        merge_list(l1, l2)

    def reorderList2(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        由于链表不能通过下标进行访问，因此使用线性表来通过下标进行访问
        """
        list_ref = []
        cur = head
        while cur:
            list_ref.append(cur)
            cur = cur.next

        i, j = 0, len(list_ref) - 1
        while i < j:
            list_ref[i].next = list_ref[j]  # 1 -> 4, 2 -> 3
            i += 1  # i -> 2, i -> 3
            list_ref[j].next = list_ref[i]  # 4 -> 2, 3 -> 3
            j -= 1  # j -> 3, j -> 2

        list_ref[i].next = None  # 末尾置空
