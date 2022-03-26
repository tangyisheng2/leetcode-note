#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :235. Lowest Common Ancestor of a Binary Search Tree.py
# @Time      :1/17/22
# @Author    :Eason Tang


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        root是所有子树的common ancestor
        1. 如果有任一子树在root上，那么LCA就是root
        2. 如果当前的子树分布在左右两侧，则LCA是当前节点
        3. 如果左右子树分布在同一侧，这LCA是不为空的节点
        """
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left
        return root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        遍历至节点p和节点q并且记录其路径
        则pq的LCA是其路径上的最后一个相同的节点
        """

        def dfs(node, target, cur_path):
            cur_path.append(node)

            if target.val > node.val:
                dfs(node.right, target, cur_path)
            elif target.val < node.val:
                dfs(node.left, target, cur_path)
            elif target.val == node.val:
                return

        p_path = []
        q_path = []

        dfs(root, p, p_path)
        dfs(root, q, q_path)

        for i in range(min(len(q_path), len(p_path))):
            if q_path[i] != p_path[i]:
                return q_path[i - 1]
            if i == len(q_path) - 1:
                return q_path[-1]
            elif i == len(p_path) - 1:
                return p_path[-1]

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Binary Search Tree中的LCA的条件为p <= LCA <= q或者p <= LCA <= q
        如果p, q < cur_node，则继续在左子树寻找；如果p, q > cur_node，则在右子树寻找

        """
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor
