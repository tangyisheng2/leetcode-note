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

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Not the same tree:
        1. value are different
        2. struct are different:
            p has left child while q not
            q has left child while q not
        """

        # if (not p and not q) or (p and q and p.val == q. val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)):
        #     return True
        # return False
        return True if (not p and not q) or (
                    p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,
                                                                                                       q.right)) else False
