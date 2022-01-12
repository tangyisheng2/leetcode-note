#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1036. Escape a Large Maze.py
# @Time      :1/10/22 9:14 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def bfs(start, end):
            q = collections.deque()
            visited = set()

            q.append((start[0], start[1]))

            while q:
                x, y = q.popleft()
                if x < 0 or x >= 1e6 or y < 0 or y >= 1e6:
                    continue

                if (x, y) in visited:
                    continue

                if (x, y) in blocked_set:
                    continue

                if len(visited) > 1e6:
                    return True

                if [x, y] == end:
                    return True

                visited.add((x, y))

                for ne_x, ne_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    q.append((ne_x, ne_y))

            return False

        import collections
        blocked_set = set(tuple(pos) for pos in blocked)
        return bfs(source, target) and bfs(target, source)


test = Solution()
test.isEscapePossible([[0, 999991], [0, 999993], [0, 999996], [1, 999996], [1, 999997], [1, 999998], [1, 999999]],
                      [0, 999997],
                      [0, 2])
