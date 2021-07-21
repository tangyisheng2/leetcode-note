# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   938. Range Sum of BST.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        """
        Tree -> DFS

        Left is smaller
        Right is bigger
        """
        self.dfs(root, low, high)
        return self.ans

    def dfs(self, node: TreeNode, low, high):
        """
        DFS
        @param node: Parent node of the Tree
        """
        if node is None:
            return None

        if low <= node.val <= high:
            self.ans += node.val

        if low < node.val:
            self.dfs(node.left, low, high)
        if node.val < high:
            self.dfs(node.right, low, high)
