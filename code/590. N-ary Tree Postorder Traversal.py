#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :590. N-ary Tree Postorder Traversal.py
# @Time      :12/28/21 9:02 PM
# @Author    :Eason Tang
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def postorder_dfs(root):
            if not root:
                return

            for child in root.children:
                postorder_dfs(child)

            ans.append(root.val)

        ans = []
        postorder_dfs(root)
        return ans

    def postorder2(self, root: 'Node') -> List[int]:
        # https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/solution/ncha-shu-de-hou-xu-bian-li-by-leetcode/
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            for child in node.children:  # For
                stack.append(child)

        return ans[::-1]
