#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :589. N-ary Tree Preorder Traversal.py
# @Time      :12/28/21 8:58 PM
# @Author    :Eason Tang
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if not root:
                return
            ans.append(root.val)
            for child in root.children:
                dfs(child)

        ans = []
        dfs(root)
        return ans
