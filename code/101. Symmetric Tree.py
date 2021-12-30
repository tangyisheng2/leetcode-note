#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :101. Symmetric Tree.py
# @Time      :12/29/21 10:12 PM
# @Author    :Eason Tang


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(root1, root2):
            """
            This function checks if root1 and root2 is inversed (symmertic)
            """
            if (root1 is None and root2) or (
                    root1 and root2 is None):  # If any side of the root is None, then the tree is not symmetric
                return False

            if root1 is None and root2 is None:  # If both side are empty, then the tree is symmetric
                return True

            if root1.val != root2.val:  # If the value is not equal, then the tree is not symmetric
                return False

            return dfs(root1.left, root2.right) and dfs(root1.right, root2.left)  # Check if the sub-tree is symmetric

        return dfs(root, root)
