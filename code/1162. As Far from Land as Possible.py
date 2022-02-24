#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1162. As Far from Land as Possible.py
# @Time      :2/23/22
# @Author    :Eason Tang
import collections
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        你可以想象成你从每个陆地上派了很多支船去踏上伟大航道，踏遍所有的海洋。
        每当船到了新的海洋，就会分裂成4条新的船，向新的未知海洋前进（访问过的海洋就不去了）。
        如果船到达了某个未访问过的海洋，那他们是第一个到这片海洋的。很明显，这么多船最后访问到的海洋，肯定是离陆地最远的海洋。
        :param grid:
        :return:
        """
        m = len(grid)
        n = len(grid[0])
        res = -1
        q = collections.deque()
        #   将所有的陆地加入队列
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j))

        #   如果全部为陆地或者全部为海洋
        if len(q) == 0 or len(q) == m * n:
            return -1

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        q.append((nx, ny))
                        #   设置为 - 1，避免再次访问
                        grid[nx][ny] = -1
            #   经过一轮遍历，结果 + 1
            res += 1

        return res


test = Solution()
test.maxDistance(grid=[[1, 0, 1], [0, 0, 0], [1, 0, 1]])
