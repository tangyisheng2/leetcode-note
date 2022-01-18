#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :257. Binary Tree Paths.py
# @Time      :1/17/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, current_state):
            nonlocal ans
            if not node:
                return 0

            if not node.left and not node.right:
                state = current_state + [node.val]
                ans.append("->".join([str(val) for val in state]))

            current_state.append(node.val)
            dfs(node.left, current_state)
            dfs(node.right, current_state)
            current_state.pop()

        ans = []
        dfs(root, [])
        return ans
