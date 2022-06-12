# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Convert the s1, s2 linkedlist to stack (note the linkedlist comes in reverse order)
        s1 = []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        s2 = []
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        ans = []
        # Initial carry is 0
        carry = 0

        for i in range(max(len(s1), len(s2))):
            # Add the numbers
            digit = ((s1[i] if i < len(s1) else 0) + (s2[i] if i < len(s2) else 0) + carry)
            # Append the last digit
            ans.append(digit % 10)
            # calculate the carry for next add
            carry = digit // 10
        # If still have a carry at the end
        if carry:
            ans.append(carry)

        # Covert ans array to linkedlist
        head = ListNode()
        cur = head

        for num in ans:
            cur.next = ListNode(num)
            cur = cur.next

        return head.next


# L1
l1 = ListNode()
l1.val = 2
l1.next = ListNode()
l1_tmp = l1.next
l1_tmp.val = 4
l1_tmp.next = ListNode()
l1_tmp = l1_tmp.next
l1_tmp.val = 3
# L2
l2 = ListNode()
l2.val = 5
l2.next = ListNode()
l2_tmp = l2.next
l2_tmp.val = 6
l2_tmp.next = ListNode()
l2_tmp = l2_tmp.next
l2_tmp.val = 4
test = Solution()
test.addTwoNumbers(l1, l2)
