#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :23. Merge k Sorted Lists.py
# @Time      :3/27/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()

        cur_node = [x for x in lists]
        res_node = head

        while any(cur_node):
            min_val = float('inf')
            min_idx = 0
            for i, node in enumerate(cur_node):
                if node and node.val < min_val:
                    min_idx = i
                    min_val = node.val
            res_node.next = cur_node[min_idx]
            res_node = res_node.next
            cur_node[min_idx] = cur_node[min_idx].next

        return head.next
