#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :210. Course Schedule II.py
# @Time      :3/13/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Use topology sort
        """
        import collections
        ans = []
        q = collections.deque()
        lastest_idx = 0

        # Create adjacency list
        adjacency = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegree[cur] += 1

        # Enqueue all the node with indegree = 0
        for course, cnt in enumerate(indegree):
            if cnt == 0:
                q.append(course)

        # print(adjacency, indegree, q)
        while lastest_idx < len(q):
            course = q[lastest_idx]
            ans.append(course)

            # "Remove the current course"
            for next_course in adjacency[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

            lastest_idx += 1

        # print(ans)

        # Check if all the course are "removed", if yes output ans, else output []
        return list(q) if len(q) == numCourses else []
