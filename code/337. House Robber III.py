#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :337. House Robber III.py
# @Time      :2/12/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        """
        直接后序DFS
        假设我们有三代的节点，爷爷，父母，子孙，一共有两种方式（当前节点在爷爷节点）
        1. 爷爷与子孙抢，则获利为node.val + ((dfs(node.left.left) + dfs(node.left.right)) if node.left else 0) + (
                (dfs(node.right.left) + dfs(node.right.right)) if node.right else 0)
                此处要注意抢子孙的时候的计算需要加上括号房子计算顺序出错
        2. 父母抢，则获利为dfs(node.left) + dfs(node.right)
        最后在父节点选择最大的一种方案
        :param root:
        :return:
        """
        def dfs(node):
            if not node:
                return 0

            method2 = dfs(node.left) + dfs(node.right)
            method1 = node.val + ((dfs(node.left.left) + dfs(node.left.right)) if node.left else 0) + (
                (dfs(node.right.left) + dfs(node.right.right)) if node.right else 0)  # 注意这里的括号，会造成运算bug

            # method1 = node.val + (dfs(node.left.left) + dfs(node.left.right)) if node.left else 0 + (dfs(node.right.left) + dfs(node.right.right)) if node.right else 0 错误示范

            """下列两行等同"""
            # if node.left:
            #     method1 += (dfs(node.left.left) + dfs(node.left.right))

            # if node.right:
            #     method1 += (dfs(node.right.left) + dfs(node.right.right))

            return max(method1, method2)

        return dfs(root)

    def rob2(self, root: TreeNode) -> int:
        """
        采用记忆化搜索
        :param root:
        :return:
        """
        memo = {}

        def dfs(node):
            if not node:
                return 0

            if node in memo:
                return memo[node]

            method2 = dfs(node.left) + dfs(node.right)
            method1 = node.val + ((dfs(node.left.left) + dfs(node.left.right)) if node.left else 0) + (
                (dfs(node.right.left) + dfs(node.right.right)) if node.right else 0)  # 注意这里的括号，会造成运算bug

            memo[node] = max(method1, method2)

            return memo[node]

        return dfs(root)

    def rob3(self, root: TreeNode) -> int:
        """

        :param root:
        :return:
        """
        def dfs(node):
            """
            节点
            当前节点选择不偷：当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
            当前节点选择偷：当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数
            :param node:
            :return: [当前节点不偷的最大获利，当前节点偷的最大获利]
            """
            if not node:
                return [0, 0]

            ans = [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)

            ans[0] = max(left[0], left[1]) + max(right[0], right[1])
            # 当前节点选择不偷：当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
            ans[1] = left[0] + right[0] + node.val
            # 当前节点选择偷：当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数

            return ans

        ans = dfs(root)
        return max(ans)
