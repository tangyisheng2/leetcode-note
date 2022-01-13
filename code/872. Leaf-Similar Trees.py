#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :872. Leaf-Similar Trees.py
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_sequence(root):
            def dfs(node):
                if not node:
                    return

                if not node.left and not node.right:
                    ans.append(node.val)
                    print(ans)

                dfs(node.left)
                dfs(node.right)

            ans = []
            dfs(root)

            return ans

        return get_leaf_sequence(root1) == get_leaf_sequence(root2)
