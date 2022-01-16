#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :112. Path Sum.py
# @Time      :1/16/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         """
#         Traditional DFS
#         """
#         def dfs(node, cur_sum):
#             """
#             This function updates found base on the current sum
#             """
#             nonlocal found
#             if not node:
#                 return False
#
#             if not node.left and not node.right:
#                 found = cur_sum + node.val == sum or found
#                 return
#
#             dfs(node.left, cur_sum + node.val)
#             dfs(node.right, cur_sum + node.val)
#
#         found = False
#         dfs(root, 0)
#         return found

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        This function reduces the target sum until the leaf node and check if the node.val is equal to sum
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)


