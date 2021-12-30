#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1302. Deepest Leaves Sum.py
# @Time      :12/29/21 9:29 PM
# @Author    :Eason Tang
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        Traverse through all the node, store the node val and the depth
        Then iterate through the result and get the sum
        """
        max_depth = 0
        temp_ans = []
        ans = 0

        def dfs(root, depth):
            nonlocal max_depth
            if not root:
                return

            max_depth = max(max_depth, depth)
            temp_ans.append((depth, root.val))

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 1)
        for record in reversed(sorted(temp_ans)):
            if record[0] == max_depth:
                ans += record[1]
            else:
                break
        return ans

    def deepestLeavesSum2(self, root: Optional[TreeNode]) -> int:
        """
        Maintain a ans and max depth variable
        Track the current depth in dfs:
        If current depth is larger than max depth: update max_depth, ans = node.val
        If current depth is equal to max depth: ans += node.val
        If current depth is less than max depth: continue traversal
        """

        def dfs(root, depth):
            nonlocal ans
            nonlocal max_depth
            if not root:
                return

            if depth == max_depth:
                ans += root.val
            elif depth > max_depth:
                max_depth = depth
                ans = root.val

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        max_depth = 0
        ans = 0
        dfs(root, 1)
        return ans