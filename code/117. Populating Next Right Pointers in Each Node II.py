#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :117. Populating Next Right Pointers in Each Node II.py
# @Time      :7/31/22
# @Author    :Eason Tang


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        使用BFS按层级遍历
        """
        if not root:
            return
        import collections
        q = collections.deque([root])

        while q:
            n = len(q)
            new_q = collections.deque()
            for i in range(n):
                if i < n - 1:
                    q[i].next = q[i + 1]
                if q[i].left:
                    new_q.append(q[i].left)
                if q[i].right:
                    new_q.append(q[i].right)
            q = new_q

        return root
