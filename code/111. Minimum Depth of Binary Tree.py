#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :111. Minimum Depth of Binary Tree.py
# @Time      :1/12/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def minDepth(self, root: TreeNode) -> int:
    #     # DFS
    #     minimum_height = int("inf")
    #
    #     def dfs(node, height):
    #         nonlocal minimum_height
    #         if not node:
    #             return
    #
    #         if not node.left and not node.right:
    #             minimum_height = min(minimum_height, height)
    #
    #         dfs(node.left, height + 1)
    #         dfs(node.right, height + 1)
    #
    #     if not root:
    #         return 0
    #     dfs(root, 1)
    #     return minimum_height

    # def minDepth(self, root: TreeNode) -> int:
    #     # BFS
    #     import collections
    #
    #     if not root:
    #         return 0
    #
    #     q = collections.deque({(root, 1)})
    #     while q:
    #         node, depth = q.popleft()
    #         if not node:
    #             continue
    #
    #         if not node.left and not node.right:
    #             return depth
    #
    #         q.append((node.left, depth + 1))
    #         q.append((node.right, depth + 1))

    def minDepth(self, root: TreeNode) -> int:
        # Recursive
        def getMinDepth(node):
            """
            This function return the min depth of the tree
            """
            if not node:
                return 0

            return min(1 + getMinDepth(node.left) if node.left else 10e6,
                       1 + getMinDepth(node.right) if node.right else 10e6)

        return getMinDepth(root)
