#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :752. Open the Lock.py
# @Time      :10/29/21 3:50 PM
# @Author    :Eason Tang
from typing import List
import collections

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        无向图，边的权重都是1，本质上是招此无向图的最短路径
        唯一的变形是加入deadend，即存在非法状态
        """
        from collections import deque
        base = [1, 10, 100, 1000]
        dead = set(int(x) for x in deadends)
        start = int('0000')
        goal = int(target)

        if start in dead:
            return -1

        if start == goal:
            return 0  # basecase

        q = collections.deque([(start, 0)])
        visited = {start}
        while q:
            node, step = q.popleft()
            for i in range(4):
                r = (node // base[i]) % 10  # 获取当前位的数字
                for j in [-1, 1]:
                    next_ = node + ((r + j + 10) % 10 - r) * base[i]
                    """
                    # 往上下扭并且计算新的节点（数）
                    ((r + j + 10) % 10 - r) * base[i] -> 与原来节点的差值
                    r + j -> 原油数字上下扭动1
                    (r + j + 10) -> 因Python对于负数取余的特殊性质，因此加10将其变为正数(e.g. -1 % 10 = 9; 1 % 10 = 1)
                    (r + j + 10) % 10 -> 因为按钮可以循环扭，因此使用取余做一个隐式的循环
                    ((r + j + 10) % 10 - r) -> 求与原来位数的差值
                    ((r + j + 10) % 10 - r) * base[i] -> 乘上对应的base
                    """
                    if next_ == goal:
                        return step + 1
                    if next_ in dead or next_ in visited:
                        continue
                    q.append((next_, step + 1))
                    visited.add(next_)
        return -1
