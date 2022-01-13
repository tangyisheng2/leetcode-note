#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :965. Univalued Binary Tree.py
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
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node):
            """
            This function traverse the tree and compare the node val to uni_value
            """
            if not node:
                return True

            if node.val != uni_value:
                return False

            return dfs(node.left) and dfs(node.right)

        if not root:
            return False

        uni_value = root.val
        return dfs(root)
