#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :19. Remove Nth Node From End of List.py
# @Time      :3/10/22
# @Author    :Eason Tang


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        1. Use pre pointer to track the previous node (set to None at first)
        2. Link the new list
        2.1 pre.next = to_delete_node.next
        2.2 to_delete_node = None

        3 case:
        1. remove the head node
        2. remove the middle node
        3. remove the last node
        4. The node to remove exceed to boundary
        """

        list_ = []

        while head:
            list_.append(head)
            head = head.next

        idx = len(list_) - n

        if idx < 0:  # Case 4
            return head
        elif idx == 0:  # Case 1
            return list_[1] if len(list_) >= 2 else None
        else:
            list_[idx - 1].next = list_[idx + 1] if idx + 1 < len(list_) else None  # Case2 and Case 3

        return list_[0]
