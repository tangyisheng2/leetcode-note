#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :129. Sum Root to Leaf Numbers.py
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
    def sumNumbers(self, root: TreeNode) -> int:
        def arr_to_int(arr):
            """
            This function converts array to integer
            """
            print(arr)
            num = 0
            for i in range(len(arr)):
                num = num * 10 + arr[i]
            return num

        def dfs(node, current_state):
            nonlocal ans
            if not node:
                return

            if not node.left and not node.right:
                # Reach the leaf node
                ans += arr_to_int(current_state + [node.val])
                return

            current_state.append(node.val)
            dfs(node.left, current_state)
            dfs(node.right, current_state)
            current_state.pop()

        ans = 0
        dfs(root, [])
        return ans
