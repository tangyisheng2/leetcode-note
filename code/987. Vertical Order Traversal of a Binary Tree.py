#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :987. Vertical Order Traversal of a Binary Tree.py
# @Time      :12/28/21 11:41 PM
# @Author    :Eason Tang
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, x, y):
            """
            traverse tree and update the val and location in (col, row, val)
            """
            if not root:
                return
            location.append((x, y, root.val))
            dfs(root.left, x - 1, y + 1)
            dfs(root.right, x + 1, y + 1)

        if not root:
            return []
        location = []
        dfs(root, 0, 0)

        location.sort()
        print(location)
        # Location: [(-1, 1, 9), (0, 0, 3), (0, 2, 15), (1, 1, 20), (2, 2, 7)]
        ans = []
        pre_x_coordnate = None  # Save the previous coordinate to judge each vertical layer
        tmp_ans = []    # temp variable to save the vertical layer traversal result
        for node in location:
            if node[0] != pre_x_coordnate:  # if current x coordinate is different from the last one -> start a new layer
                if tmp_ans:
                    ans.append(tmp_ans)
                    # Only append when there is result in temp_ans to skip the initial empty temp_ans caused by the initial None value of pre_x_coordinate and root
                tmp_ans = []    # Reset temp_ans for next vertical level
                pre_x_coordnate = node[0]   # Update x_coordinate
            tmp_ans.append(node[2])
        ans.append(tmp_ans) # Push the last temp_ans to ans
        return ans
