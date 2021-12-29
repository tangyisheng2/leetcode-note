#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :145. Binary Tree Postorder Traversal.py
# @Time      :12/28/21 6:29 PM
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        dfs(root)
        return ans
