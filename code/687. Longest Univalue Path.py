#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :687. Longest Univalue Path.py
# @Time      :2/3/22
# @Author    :Eason Tang
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def getLongestValue(node):
            """
            This function returns the longest path count and the value pass the root and update the longest value
            """
            nonlocal ans
            if not node:
                return 0, None
            # Calculate the left and right length
            left, val_l = getLongestValue(node.left)
            right, val_r = getLongestValue(node.right)
            left_uni, right_uni = 0, 0
            # If left node is valid, uni length = left + 1
            if val_l == node.val:
                left_uni = left + 1
            # If right node is valid, uni length = right + 1
            if val_r == node.val:
                right_uni = right + 1
            # Update the longest length
            ans = max(ans, left_uni + right_uni)
            # For parent node, the maximun length this node provide is
            return max(left_uni, right_uni), node.val

        ans = 0
        getLongestValue(root)
        return ans
