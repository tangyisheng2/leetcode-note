#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :133. Clone Graph.py
# @Time      :2/12/22
# @Author    :Eason Tang
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            """
            This function traverse through the original map and make a deep copy
            """
            if not node:
                return

            if node in visited:  # 如果克隆的节点已经存在，直接返回克隆的节点
                return visited[node]

            new_clone_node = Node(node.val, [])  # 如果克隆节点不存在，则新建克隆的节点

            visited[node] = new_clone_node  # 将刚刚新建的节点放入visited哈希表，防止重复新建

            if node.neighbors:  # 如果原始节点有邻居
                new_clone_node.neighbors = [dfs(neighbour) for neighbour in node.neighbors]  # 对邻居进行克隆

            return new_clone_node  # 返回头节点

        visited = {}
        return dfs(node)
