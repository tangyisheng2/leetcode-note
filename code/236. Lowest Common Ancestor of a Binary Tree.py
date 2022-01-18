#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :236. Lowest Common Ancestor of a Binary Tree.py
# @Time      :1/17/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def dfs(node):
#             nonlocal ans, found_p, found_q
#             if not node:
#                 return
#
#             dfs(node.left)
#             dfs(node.right)
#
#
#
#             if node.val == p.val:
#                 found_p = True
#
#             if node.val == q.val:
#                 found_q = True
#
#             # if found_p and found_q and not ans.val:
#             #     # 这里需要ans.val为空的原因是因为我们寻找Lowest Common Ancestor，因此当ans.val有值时不应该更新
#             #     ans = node
#             #     return
#
#             if found_p and found_q and not ans.val:
#                 ans = node
#                 return node
#
#             if (found_p and node.val == q.val) or (found_q and node.val == q.val):
#                 ans = node
#                 return node
#
#         found_p = False
#         found_q = False
#         ans = TreeNode(None)
#         dfs(root)
#         return ans
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        祖先的定义：若节点p在root的左右子树中，或者root == p，则root是p的祖先
        则root的左右孩子不是p, q的最近公共祖先，则root是p, q的最近公共祖先。
        0. 不存在LCA
        存在的时候分为三种情况：
        1. p, q分别在root的两侧
        2. p, q在root的左侧（right不存在）
        3. p, q在root的右侧（left不存在）
        """
        if not root or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None # 1. 如果不存在LCA
        if not left:
            return right  # 3. 如果LCA在左子树
        if not right:
            return left  # 4. 如果LCA在又子树
        return root  # 2. 如果LCA分别在左右子树


# root = TreeNode(3)
# root.left = TreeNode(5)
# root.left.left = TreeNode(6)
# root.left.right = TreeNode(2)
# root.left.right.left = TreeNode(7)
# root.left.right.right = TreeNode(4)
# root.right = TreeNode(1)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(8)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

test = Solution()
ret = test.lowestCommonAncestor(root, TreeNode(2), TreeNode(3))
