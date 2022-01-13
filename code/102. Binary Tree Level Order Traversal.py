#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :102. Binary Tree Level Order Traversal.py
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        import collections
        q = collections.deque()
        q.append((root, 1))
        ans = []

        current_node_list = []
        current_depth = 1

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
        return ans


test = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
test.levelOrder(root)
