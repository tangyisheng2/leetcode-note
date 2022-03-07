#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :141. Linked List Cycle.py
# @Time      :3/7/22
# @Author    :Eason Tang
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Use visited to keep track of the visited node
        """
        ans = False
        visited = set()
        cur_node = head
        visited.add(cur_node)
        while cur_node and cur_node.next and not ans:
            cur_node = cur_node.next
            if cur_node in visited:
                ans = True
            visited.add(cur_node)
        return ans

    def hasCycle2(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
