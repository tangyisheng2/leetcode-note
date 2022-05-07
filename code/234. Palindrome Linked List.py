#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :234. Palindrome Linked List.py
# @Time      :5/6/22
# @Author    :Eason Tang


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        ptrl = 0
        ptrr = len(arr) - 1

        while ptrl < ptrr:
            if arr[ptrl] != arr[ptrr]:
                return False

            ptrl += 1
            ptrr -= 1

        return True

    def isPalindrome2(self, head: ListNode) -> bool:

        front_pointer = head  # 记录正向的pointer

        def recursively_check2(node):
            """
            Kinda works like a post-order traversion
            This function iterates through the linked list and compare the leaf node with front pointer
            if they are the same, return True, else False
            if the previous compare is false, the linked list is not longer palidrome, so return false
            else (for valid situation) return True
            """
            nonlocal front_pointer
            if not node:
                return True  # Empty linked list is palidrome

            if not recursively_check2(node.next):
                # If the previous compared is False
                return False

            if front_pointer.val != node.val:
                # If the current compare false, return False
                return False

            front_pointer = front_pointer.next  # Update the front pointer
            return True  # For other valid situation, return True

        return recursively_check2(head)
