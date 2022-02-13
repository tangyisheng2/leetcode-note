#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :138. Copy List with Random Pointer.py
# @Time      :2/12/22
# @Author    :Eason Tang
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node):
            """
            This function traverse through the link and make a copy
            """
            if not node:
                return None

            if node in visited:  # 如果节点已经克隆了，直接返回克隆的节点
                return visited[node]

            node_cp = Node(node.val, None, None)  # 如果节点没有克隆，则克隆新节点
            visited[node] = node_cp  # 马上将其加入visited
            node_cp.next = dfs(node.next)  # 克隆节点的next是原节点next的克隆
            node_cp.random = dfs(node.random)  # 克隆节点的random是原节点random的克隆

            return node_cp  # 返回头节点

        visited = {}
        return dfs(head)
