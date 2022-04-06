#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :310. Minimum Height Trees.py
# @Time      :4/5/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [-1] * n

        def bfs(start: int):
            vis = [False] * n
            vis[start] = True
            q = deque([start])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parents[y] = x
                        q.append(y)
            return x

        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        """
        使用parents数组来存储bfs中的路径
        令y为当前节点的下标（同时也是节点的值），则parents[y]的值为y的父节点，如有
        start = 2， end = 5, parents = [3, 3, 3, 4, 5, -1]
        1. 首先要将parent[end] = -1，作为退出的标志
        2. 从起点出发遍历
            parent[2] = 3
            parent[3] = 4
            parent[4] = 5
            parent[5] = -1 -> 跳出
        3. 得到path为[2, 3, 4, 5]
        """
        parents[x] = -1
        print(x, y, parents)
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        print(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]


test = Solution()
test.findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]])
