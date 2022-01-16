#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :113. Path Sum II.py
# @Time      :1/16/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, cur_sum, cur_path):
            if not node:
                return

            if cur_sum + node.val == targetSum and not node.left and not node.right:
                ans.append(cur_path[:] + [node.val])
                return

            dfs(node.left, cur_sum + node.val, cur_path + [node.val])
            dfs(node.right, cur_sum + node.val, cur_path + [node.val])

        ans = []
        dfs(root, 0, [])
        return ans
