#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :606. Construct String from Binary Tree.py
# @Time      :3/18/22
# @Author    :Eason Tang
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        递归方法
        设tree2str返回构造好的子数组
        共有3种情况：
        Case1: 左右孩子均不存在，直接返回根节点
        Case2：左孩子不存在，返回"{root.val}(){tree2str(root.right)}"
            注意由于存在二义性，因此"()"不能省略
        Case3：右孩子不存在，返回{root.val}{tree2str(root.left)}
        :param root:
        :return:
        """
        if not root:
            return ''

        if not root.left and not root.right:
            return str(root.val)

        if not root.right:
            return f'{root.val}({self.tree2str(root.left)})'

        return f'{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})'
