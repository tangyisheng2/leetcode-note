#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :144. Binary Tree Preorder Traversal.py
# @Time      :12/20/21 11:05 PM
# @Author    :Eason Tang
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], current_stat: List):
            """
            Return the preorder traversal result
            """
            if root == None:
                return []

            current_stat.append(root.val)

            dfs(root.left, current_stat)
            dfs(root.right, current_stat)

            return current_stat

        return dfs(root, [])
