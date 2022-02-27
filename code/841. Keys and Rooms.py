#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :841. Keys and Rooms.py
# @Time      :2/26/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        BFS
        :param rooms:
        :return:
        """
        import collections
        q = collections.deque()
        visited = set()

        q.append(0)
        visited.add(0)

        while q:
            room = q.popleft()

            for key in rooms[room]:
                if key not in visited:
                    q.append(key)
                    visited.add(key)

        return len(visited) == len(rooms)

    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        """
        DFS
        :param rooms:
        :return:
        """

        def dfs(idx):
            for room in rooms[idx]:
                if room not in visited:
                    visited.add(room)
                    dfs(room)

        visited = set({0})
        dfs(0)
        return len(visited) == len(rooms)
