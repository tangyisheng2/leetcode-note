#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :110. Balanced Binary Tree.py
# @Time      :12/29/21 11:26 PM
# @Author    :Eason Tang
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def getHeight(root):
            """
            This function will retrun the maximun height of sub children
            If the tree is not a balanced tree, we return -1
            """
            if not root: return 0  # If tree is empty, then the height is 0
            lh = getHeight(root.left)  # Calculate the left height
            if lh == -1: return -1
            rh = getHeight(root.right)  # Calculate the right height
            if rh == -1: return -1
            if abs(lh - rh) > 1: return -1  # If any of the left right tree is not a balanced tree, return -1
            return max(lh, rh) + 1

        return getHeight(root) != -1
