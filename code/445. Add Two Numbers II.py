#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :445. Add Two Numbers II.py
# @Time      :2021/7/2 11:49 PM
# @Author    :Eason Tang


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        观察到连标的数字从高位到低位，而我们在计算加法时一般从低位到高位，顺序刚好相反
        因此我们使用链表来进行计算
        :param l1:
        :param l2:
        :return:
        """
        num1_stack = []
        num2_stack = []
        res_stack = []
        carry = 0

        while l1:   # 将l1节点放序
            num1_stack.append(l1.val)
            l1 = l1.next

        while l2:   # l2节点数字反序
            num2_stack.append(l2.val)
            l2 = l2.next

        while num1_stack or num2_stack:
            num1 = num1_stack.pop() if num1_stack else 0    # l1数字出栈
            num2 = num2_stack.pop() if num2_stack else 0

            res = (num1 + num2 + carry) % 10
            res_stack.append(res)

            carry = (num1 + num2 + carry) // 10

        if carry:
            res_stack.append(1)

        res_head = ListNode()
        res_ptr = res_head
        while res_stack:
            res_ptr.val = res_stack.pop()
            if res_stack:
                res_ptr.next = ListNode()
                res_ptr = res_ptr.next

        return res_head


l1 = [8, 9, 9]
l2 = [2]
l1_head = ListNode(val=l1[0])
l1_ptr = l1_head
for i in range(1, len(l1)):
    l1_ptr.next = ListNode()
    l1_ptr = l1_ptr.next
    l1_ptr.val = l1[i]

l2_head = ListNode(val=l2[0])
l2_ptr = l2_head
for i in range(1, len(l2)):
    l2_ptr.next = ListNode()
    l2_ptr = l2_ptr.next
    l2_ptr.val = l2[i]

test = Solution()
test.addTwoNumbers(l1=l1_head, l2=l2_head)
