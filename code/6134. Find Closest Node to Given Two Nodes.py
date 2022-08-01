#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :6134. Find Closest Node to Given Two Nodes.py
# @Time      :7/30/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        dist_1 = {}  # 使用dict存储起点到其他店的距离
        dist_2 = {}

        def dfs(node, visited, dist, cur_dist):
            """
            使用DFS计算该点到其他点的距离（因为每一个节点只有一条出边）
            """
            if node in visited:
                return -1

            dist[node] = cur_dist
            visited.add(node)
            if edges[node] != -1:
                dfs(edges[node], visited, dist, cur_dist + 1)

        def bfs(node, visited, dist):
            import collections
            q = collections.deque([(node, 0)])

            while q:
                node, cur_dist = q.popleft()

                visited.add(node)
                dist[node] = cur_dist

                if edges[node] != -1 and edges[node] not in visited:
                    q.append((edges[node], cur_dist + 1))

        # DFS会比BFS稍微快一点
        dfs(node1, set(), dist_1, 0)
        dfs(node2, set(), dist_2, 0)

        # bfs(node1, set(), dist_1)
        # bfs(node2, set(), dist_2)

        min_dist = float('inf')
        min_point = None

        for key in dist_1:
            if key in dist_2:
                if max(dist_1[key], dist_2[key]) < min_dist:  # 注意题目问题是使两点距离中的“较大点”最小化
                    min_dist = max(dist_1[key], dist_2[key])
                    min_point = key
                elif max(dist_1[key], dist_2[key]) == min_dist:
                    min_point = min(min_point, key)

        return min_point if min_point is not None else -1  # 需要注意min_point可能为代码0，因此需要特别判定是否为None


test = Solution()
ret = test.closestMeetingNode([4, 4, 8, -1, 9, 8, 4, 4, 1, 1],
                              5,
                              6)
print(ret)
