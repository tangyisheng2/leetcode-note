#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :108. Convert Sorted Array to Binary Search Tree.py
# @Time      :4/9/22
# @Author    :Eason Tang
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if not nums:
            return None

        mid = l // 2
        root = TreeNode(nums[mid])
        if mid - 1 >= 0:
            # 左边部分的数组结束下标
            root.left = self.sortedArrayToBST(nums[:mid])
        if mid + 1 < l:
            # 右边部分的开始下标
            root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
