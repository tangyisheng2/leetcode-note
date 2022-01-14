#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :814. Binary Tree Pruning.py
# @Time      :1/13/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        This function prunes tree recursively
        Since we need to judge if the node and its sub-tree contain 0 only, then we prune the current node. So we use the post-order traversal
        """
        if not root:
            return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not root.left and not root.right and root.val == 0:
            # Here we prune the node,
            return None

        return root
