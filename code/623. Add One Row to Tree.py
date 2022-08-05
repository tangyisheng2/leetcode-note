#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :623. Add One Row to Tree.py
# @Time      :8/4/22
# @Author    :Eason Tang
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """
        1. Traverse through the tree using bfs to the depth - 1
        2. connect the new node to the node in queue, and their children
        """
        if not root:
            return

        if depth == 1:
            return TreeNode(val=val, left=root)

        import collections
        q = collections.deque([(root, 1)])  # (node, depth starting from 1)

        while q:
            cur_depth = q[0][1]
            if cur_depth >= depth:  # early stop, the new layer will be on the level of parameter death, when we traverse to this layer, we can tell that the node has been added
                return root
            new_q = collections.deque()
            for elem in q:
                node = elem[0]
                if cur_depth == depth - 1:
                    node.left = TreeNode(val=val, left=node.left if node else None)
                    node.right = TreeNode(val=val, right=node.right if node else None)

                if node.left:
                    new_q.append((node.left, cur_depth + 1))
                if node.right:
                    new_q.append((node.right, cur_depth + 1))

            q = new_q
