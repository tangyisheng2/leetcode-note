#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :427. Construct Quad Tree.py
# @Time      :4/28/22
# @Author    :Eason Tang
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct1(self, grid: List[List[int]]) -> 'Node':
        """
        Use recurrsion
        Base case:
        - When the subgrid is 1*1: return Node(isLeaf = True)
        - When the subgrid is 2*2: return a node with 4 children-Node(isLeaf = True),
            and if the val of 4 childrens is the same and isLeaf == Ture,
            set currentNode.isLeaf = True
            (Optinal: set all 4 childrens to None)

        1. determine the split point: len(n) // 2
        2. Add the subgrid to the root as a Node()
        """

        def dfs(subgrid):
            # if len(subgrid) == 1:
            #     return Node(val=subgrid[0][0], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None,
            #                 bottomRight=None)

            if all([subgrid[i][j] == subgrid[0][0] for i in range(len(subgrid)) for j in range(len(subgrid))]):
                return Node(val=subgrid[0][0], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None,
                            bottomRight=None)

            n = len(subgrid)  # n = 4
            top_left = [x[:n // 2] for x in subgrid[:n // 2]]  # [x[:2] for x in subgrid[:2]]
            top_right = [x[n // 2:] for x in subgrid[:n // 2]]  # [x[2:] for x in subgrid[:2]]
            bottom_left = [x[:n // 2] for x in subgrid[n // 2:]]  # x[2:] for x in subgrid[2:]]
            bottom_right = [x[n // 2:] for x in subgrid[n // 2:]]  # x[2:] for x in subgrid[2:]]
            new_node = Node(val=0, isLeaf=False, topLeft=dfs(top_left), topRight=dfs(top_right),
                            bottomLeft=dfs(bottom_left), bottomRight=dfs(bottom_right))

            if all([x.isLeaf == True for x in
                    [new_node.topLeft, new_node.topRight, new_node.bottomLeft, new_node.bottomRight]]) and len(
                set([x.val for x in
                     [new_node.topLeft, new_node.topRight, new_node.bottomLeft, new_node.bottomRight]])) == 1:
                new_node.isLeaf = True
                new_node.val = subgrid[0][0]
                new_node.topLeft = None
                new_node.topRight = None
                new_node.bottomLeft = None
                new_node.bottomRight = None

            return new_node

        return dfs(grid)

    def construct2(self, grid: List[List[int]]) -> 'Node':
        """
        Use recurrsion
        Base case:
        - When the subgrid is 1*1: return Node(isLeaf = True)
        - When the subgrid is 2*2: return a node with 4 children-Node(isLeaf = True),
            and if the val of 4 childrens is the same and isLeaf == Ture,
            set currentNode.isLeaf = True
            set all 4 childrens to None
        - *Another way is to check if every elements in the matrix are the same

        1. determine the split point: len(n) // 2 (Also can do in a index way)
        2. Add the subgrid to the root as a Node()

        *Optimization: Use prefix sum matrix to avoid redo the equal check in every sub grid
        """

        n = len(grid)
        # Prefix Sum matrix
        pre = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1] + grid[i - 1][j - 1]

        def getSum(r0: int, c0: int, r1: int, c1: int) -> int:
            return pre[r1][c1] - pre[r1][c0] - pre[r0][c1] + pre[r0][c0]

        def dfs(r0: int, c0: int, r1: int, c1: int) -> 'Node':
            """
            r0, r1: boundary of the sub matrix
            c0, c1: boundary of the sub matrix
            """
            total = getSum(r0, c0, r1, c1)
            if total == 0:
                return Node(False, True)
            if total == (r1 - r0) * (c1 - c0):
                return Node(True, True)
            return Node(
                True,
                False,
                dfs(r0, c0, (r0 + r1) // 2, (c0 + c1) // 2),
                dfs(r0, (c0 + c1) // 2, (r0 + r1) // 2, c1),
                dfs((r0 + r1) // 2, c0, r1, (c0 + c1) // 2),
                dfs((r0 + r1) // 2, (c0 + c1) // 2, r1, c1),
            )

        return dfs(0, 0, n, n)
