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


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         """
#         使用pre, cur存储前序节点和当前节点，并且依次遍历
#         """
#         if not head:
#             return []
#
#         cur = head
#         pre = None
#         while cur:
#             next = cur.next  # 在更改了下面节点后，需要存储原先的节点
#             cur.next = pre
#             pre = cur
#             cur = next
#
#         return pre

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        1 -> 2 -> 3 -> 4 -> 5

        1 -> 2 -> 3 -> [4 <- 5]
                  ^
                  head
        head.next.next = head
        head.next = None
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head  # 反转当前子列表的指针到当前递归的头节点
        head.next = None  # 反转后的节点末尾为None
        return newHead
