#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :124. Binary Tree Maximum Path Sum.py
# @Time      :2/3/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            """
            This function calculates the maximun gain of tree root
            """
            nonlocal ans
            if not root:
                return 0

            # Calculate the gain for left root, if the child have a negative gain, ignore it
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            # The maximum sum the subtree with root = left + right + val, update it with the ans
            ans = max(ans, left + right + root.val)

            # To the parent, the subtrees gain is val + the max gain between left and right
            return root.val + max(left, right)

        ans = float('-inf')
        dfs(root)

        return int(ans)
