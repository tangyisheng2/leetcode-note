#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :508. Most Frequent Subtree Sum.py
# @Time      :1/31/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def dfs(root):
            """
            This function returns the height of the sub-tree of root
            and update it to our hashmap
            """
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            ans = left + right + root.val
            sum_ans[ans] += 1
            return ans

        if not root:
            return []

        import collections
        sum_ans = collections.defaultdict(int)
        dfs(root)
        max_freq = 0
        ans = []
        print(sum_ans)
        for sum_, cnt in sum_ans.items():
            if cnt > max_freq:
                max_freq = cnt
                ans = [sum_]
            elif cnt == max_freq:
                ans.append(sum_)
        return ans
