#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :100. Same Tree.py
# @Time      :12/29/21 9:54 PM
# @Author    :Eason Tang
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(root1, root2):
            """
            This function will return if root1 == root2
            """
            if not (root1 or root2):  # Both tree are empty
                return True

            if (not root1 and root2) or (root1 and not root2):  # Either root1 or root2 is empty, but not both
                return False

            if root1.val != root2.val:  # Root1 not equal to root2
                return False

            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(p, q)
