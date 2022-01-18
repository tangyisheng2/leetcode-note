#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :235. Lowest Common Ancestor of a Binary Search Tree.py
# @Time      :1/17/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left
        return root
