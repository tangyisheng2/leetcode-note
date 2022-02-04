#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :543. Diameter of Binary Tree.py
# @Time      :2021/7/4 12:27 AM
# @Author    :Eason Tang


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_depth = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs_depth(node: TreeNode) -> int:
            """
            计算该节点左右孩子的深度和，此时经过此节点的最长路径为左孩子的最长路径 + 右孩子的最长路径 + 1(节点自身)
            小贪心：在返回的时候，我们要选择该节点左孩子和右孩子中较长的一段路径长度返回，这样才能保证我们最后的路径一定是最长的
            :param node: 头节点
            :return: 左右节点的深度和(int)
            """
            if node is None:
                return 0
            L = dfs_depth(node.left)
            R = dfs_depth(node.right)
            self.max_depth = max(self.max_depth, L + R + 1)
            return max(L, R) + 1

        dfs_depth(root)
        return self.max_depth

    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        def diameter(root):
            nonlocal ans
            if not root:
                return 0

            left = diameter(root.left)
            right = diameter(root.right)
            # Inside the subtree, the diameter is 1 + left + right, update the ans
            diame = 1 + left + right
            ans = max(ans, diame)
            # Outside the subtree, the contributed diameter is 1 + max length between left and right
            return 1 + max(left, right)

        ans = 0
        diameter(root)
        return ans - 1
