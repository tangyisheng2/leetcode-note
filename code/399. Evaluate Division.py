#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :399. Evaluate Division.py
# @Time      :4/25/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        u, N, ans = self.Union(equations), len(equations), []
        for i in range(N):
            u.union(equations[i][0], equations[i][1], values[i])

        for x, y in queries:
            ans.append(u.isConnected(x, y))
        return ans

    class Union:
        def __init__(self, equations):
            """
            初始化：
            使用一个字典表示节点的父母self.parent[当前节点] = parent
            使用一个字典表示当前节点到根节点的权重self.parent[当前节点] = weight
            对于每一个节点，初始化状态为自己的父母是自己，权重为1
            :param equations:
            """
            self.parent, self.weight = {}, {}  # 父节点，节点到父节点的权重
            for nodes in equations:
                for x in nodes:
                    if x not in self.parent:  # 如果x没有添加到父节点中
                        self.parent[x], self.weight[x] = x, 1  # x的父节点为自身，x到父节点的权重为1

        def find(self, x):
            """
            如果x节点的父母不为自身，则依次向上寻找父母，更新父母记录以及权重，并且返回根节点
            如果x节点的父母为自己（x自成一个union）则直接返回x
            如果x的父母为
            :param x:
            :return:
            """
            if self.parent[x] != x:  # 如果x的父节点不为自身
                parent = self.parent[x]  # 当前节点的父母
                self.parent[x] = self.find(parent)  # 向上寻找上一层的父母（此递归最终会寻找到根节点的父母），更新当前节点的父亲节点
                self.weight[x] *= self.weight[parent]  # 更新当前节点到父亲节点的权重
            return self.parent[x]

        def union(self, x, y, value):
            """
            将两个节点合并到一个union中
            首先判断两个节点的父母是否相同，如果不相同，将其中一个节点的父母设为另一个节点的根
            :param x:
            :param y:
            :param value:
            :return:
            """
            rootX = self.find(x)  # 路经压缩
            rootY = self.find(y)  # 路经压缩
            if rootX != rootY:  # 如果两者的根不同，则进行合并
                self.parent[rootX] = rootY  # 将x的parent设置为y
                self.weight[rootX] = self.weight[y] * value / self.weight[x]  # 更新x到根节点的权重

        def isConnected(self, x, y):
            """
            判断x，y是否属于一个union：
            如果x, y的parent是同一个，则为同一个union
            如果
            :param x:
            :param y:
            :return:
            """
            if x in self.parent and y in self.parent:
                rootX, rootY = self.find(x), self.find(y)
                if rootX == rootY:
                    return self.weight[x] / self.weight[y]
            return -1
