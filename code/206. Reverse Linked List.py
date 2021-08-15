# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   206. Reverse Linked List.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        使用pre, cur存储前序节点和当前节点，并且依次遍历
        """
        if not head:
            return []

        cur = head
        pre = None
        while cur:
            next = cur.next  # 在更改了下面节点后，需要存储原先的节点
            cur.next = pre
            pre = cur
            cur = next

        return pre
