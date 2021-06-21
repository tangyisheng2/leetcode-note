#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1448. Count Good Nodes in Binary Tree.py
# @Time      :2021/6/21 2:40 PM
# @Author    :Eason Tang

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0  # Root node is always considered as a good node, but since we will append root node to our queue,
        # let's set initial count to 0

        queue = collections.deque()  # (node, maximun value from root to node)
        queue.append((root, root.val))
        while queue:
            node, max_value = queue.popleft()
            if node is None:    # when node is None, just skip to next node
                continue
            if node.val >= max_value:   # check if the node match the definition of good node
                count += 1
                max_value = node.val
            queue.append((node.left, max_value))    # append child node to queue
            queue.append((node.right, max_value))

        return count
