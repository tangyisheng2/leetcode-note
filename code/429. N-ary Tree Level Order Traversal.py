#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :429. N-ary Tree Level Order Traversal.py
# @Time      :12/28/21 8:38 PM
# @Author    :Eason Tang
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Because this is a level order traversal, so we use bfs
        if not root:  # if the root is empty, simply return an empty array
            return []
        import collections
        ans = []
        q = collections.deque()  # create a queue for bfs
        depth = 1  # use depth var to track the depth of each node
        q.append((root, depth))
        tmp_ans = []  # temp answer for each level
        while q:
            node, cur_depth = q.popleft()
            if cur_depth != depth:  # if the current node depth is not equal the previous one, push tmp_ans to ans
                ans.append(tmp_ans)
                depth = cur_depth
                tmp_ans = []
            tmp_ans.append(node.val)
            for child in node.children:
                q.append((child, cur_depth + 1))
        ans.append(tmp_ans)  # push the last tmp_ans to ans
        return ans
