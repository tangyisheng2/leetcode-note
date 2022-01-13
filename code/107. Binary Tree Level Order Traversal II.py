#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :107. Binary Tree Level Order Traversal II.py
# @Time      :1/13/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        import collections
        q = collections.deque({(root, 1)})
        ans = []

        current_depth = 1
        current_node_list = []

        while q:
            node, depth = q.popleft()
            if not node:
                continue

            if depth > current_depth:
                ans.append(current_node_list)
                current_node_list = []
                current_depth = depth

            current_node_list.append(node.val)

            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))

        ans.append(current_node_list)
        return ans[::-1]
