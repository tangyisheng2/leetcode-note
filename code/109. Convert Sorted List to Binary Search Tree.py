#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :109. Convert Sorted List to Binary Search Tree.py
# @Time      :7/19/22
# @Author    :Eason Tang
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getMid(left, right):
            # Slow, Fast pointer to get the mid node
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build(left, right):
            # Two pointer intersects -> No valid range
            if left == right:
                return None

            mid = getMid(left, right)  # Get the mid node as root of the tree
            root = TreeNode(mid.val)
            root.left = build(left, mid)  # Build the left child
            root.right = build(mid.next, right)  # Build the right child
            return root

        return build(head, None)  # Note: The end of the linkedlist is a None


class Solution2:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def getLength(head) -> int:
            ret = 0
            while head:
                ret += 1
                head = head.next
            return ret

        def build(left: int, right: int) -> TreeNode | None:
            """
            1. left > right: not a valid tree, return None
            2. left = right: only one node, return root = head.val
            3. has 2 node: mid = node[1], left node Case#1, right node Case#2
            4. has 3 node: mid = node[1], left node Case#2, right node Case#2
            """
            nonlocal head
            if left > right:
                return None

            mid = (left + right + 1) // 2
            root = TreeNode()  # Root placeholder

            root.left = build(left, mid - 1)  # Build the left tree

            root.val = head.val  # Populate the root node
            head = head.next

            root.right = build(mid + 1, right)  # Build the right tree

            return root

        length = getLength(head)
        return build(0, length - 1)
