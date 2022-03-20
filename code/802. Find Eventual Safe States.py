#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :802. Find Eventual Safe States.py
# @Time      :3/19/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        State:
        1. not visite
        2. node is in the current call stack (unsafe, can cause cycle)
        3. node is not in the current call stack (safe)
        """
        n = len(graph)
        state = [0] * n

        def safe(idx):
            """
            This function checks if a node is safe using dfs
            returns True if safe
            A node connected to all safe node is safe, else not safe
            """
            if state[idx]:
                return state[idx] == 2

            # when state == 0
            state[idx] = 1

            for ne in graph[idx]:
                if not safe(ne):
                    return False

            state[idx] = 2
            return True

        ans = []
        for i in range(n):
            if safe(i):
                ans.append(i)
        return ans

    def eventualSafeNodes2(self, graph: List[List[int]]) -> List[int]:
        """
        A safe node is not in a cycle ->
        use top sort to detect cycle,
        all ndoes with 0-outdegree or connected to 0 out-degree node are safe

        Implementation:
        1. reverse the map
        2. use top sort
        3. all node with 0 indegree are our answer
        """
        import collections
        n = len(graph)

        # 1. reverse the map
        adj_rev = collections.defaultdict(list)
        indegree = [0] * n
        for start_idx, start in enumerate(graph):
            for end_idx in start:
                adj_rev[end_idx].append(start_idx)
                indegree[start_idx] += 1

        # 2. top sort
        q = collections.deque()
        visited = set()

        # 2.1 enqueue all node w/ 0 in-degree
        for i, cnt in enumerate(indegree):
            if not cnt:
                q.append(i)
                visited.add(i)

        # 2.2 run top sort:
        while q:
            cur_node = q.popleft()

            for ne in adj_rev[cur_node]:
                # 不需要visited数组，因为已经统计了入度切每个点的入度为0的次数只有一次
                visited.add(ne)
                indegree[ne] -= 1
                if indegree[ne] == 0:
                    q.append(ne)

        # 3. output
        ans = []
        for i, cnt in enumerate(indegree):
            if not cnt:
                ans.append(i)
        return ans
