#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :572. Subtree of Another Tree.py
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
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSameTree(node, compare_node):
            """
            This function returns if the node is the same as compare_node
            :param node: source
            :param compare_node: compare to target
            :return: If the two tree is the same
            """
            if not node and not compare_node: return True
            if not compare_node or not node: return False

            return node.val == compare_node.val and isSameTree(node.left, compare_node.left) and isSameTree(node.right,
                                                                                                            compare_node.right)

        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        # Check
        # 1. The current node is the same as subTree
        # 2. left child contains subTree
        # 3. right child contains subTree
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
