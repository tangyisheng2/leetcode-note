#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :979. Distribute Coins in Binary Tree.py
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """
            This function returns a total move to make every node have exactly one coin
            return move_need, cnt
            """
            if not node:
                return 0, 0

            left, cnt_l = dfs(node.left)  # 左边节点移动的步数、以及扔给别人的硬币
            right, cnt_r = dfs(node.right)  # 左边节点移动的步数、以及扔给别人的硬币

            cnt = node.val + cnt_l + cnt_r - 1  # 目前该节点接受的硬币为自身硬币加左右节点给的硬币，留下一枚，剩下cnt甩给父节点
            # cnt可以为负数，此时表示该节点要向父节点取硬币
            move = left + right + abs(cnt)  # （对于初始状态）父节点要把所有硬币甩走的步数为左右节点的步数加自身硬币数量 - 1

            return move, cnt

        ans = dfs(root)[0]

        return ans
