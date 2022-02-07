#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :968. Binary Tree Cameras.py
# @Time      :2/6/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        """
        https://leetcode-cn.com/problems/binary-tree-cameras/solution/968-jian-kong-er-cha-shu-di-gui-shang-de-zhuang-ta/
        :param root:
        :return:
        """
        NOT_COVERED = 0  # 没有覆盖
        COVERED = 1  # 有覆盖
        HAS_CAMERA = 2  # 有摄像头

        def dfs(node):
            """
            This function traverse through the tree and check the camera
            """
            nonlocal ans
            if not node:
                """
                对于空节点，应该设为有覆盖
                若设为无覆盖，则叶子结点应该安装摄像头，与在父节点安装摄像头的宗旨违背
                若设为有摄像头，则叶子节点的父节点并不需要安装摄像头（即摄像头应该安装在爷爷节点），也与事实不符
                """
                return COVERED

            left = dfs(node.left)
            right = dfs(node.right)

            if left == COVERED and right == COVERED:
                """
                如果左右都有cover到的情况下，根节点就不需要放摄像头了（会在最后判断根节点是否有覆盖及是否需要放摄像头）
                """
                return NOT_COVERED

            if left == NOT_COVERED or right == NOT_COVERED:
                """
                如果左右任意节点没有覆盖，那么需要放置摄像头来进行覆盖
                """
                ans += 1
                return HAS_CAMERA

            if left == HAS_CAMERA or right == HAS_CAMERA:
                """
                如果左右任一节点有摄像头，则当前节点已经覆盖了
                """
                return COVERED

            return -1

        ans = 0
        # 递归结束之后，还要判断根节点，如果没有覆盖则还需要放置摄像头
        if dfs(root) == NOT_COVERED:
            ans += 1
        return ans
