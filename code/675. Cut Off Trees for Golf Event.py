#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :675. Cut Off Trees for Golf Event.py
# @Time      :10/29/21 6:11 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        import collections
        m = len(forest)
        n = len(forest[0])
        ans = 0
        # 0. 如果开始的时候就是封死的？
        if forest[0][0] == 0:
            return -1

        # 1. 构建要cut的数的队列
        forest_rank = []
        for x in range(m):
            for y in range(n):
                if forest[x][y] != 0:
                    forest_rank.append((forest[x][y], x, y))
        forest_rank.sort()

        # 2. 进行bfs
        def bfs(forest, start, end):
            if start == end:
                return 0

            s1, s2 = start
            e1, e2 = end

            q = collections.deque([(s1, s2, 0)])
            visited = {(s1, s2)}

            while q:
                cur_x, cur_y, step = q.popleft()
                if cur_x == e1 and cur_y == e2:
                    return step

                for ne_x, ne_y in [(cur_x + 1, cur_y), (cur_x - 1, cur_y), (cur_x, cur_y + 1), (cur_x, cur_y - 1)]:
                    if 0 <= ne_x < m and 0 <= ne_y < n and forest[ne_x][ne_y] != 0 and (ne_x, ne_y) not in visited:
                        q.append((ne_x, ne_y, step + 1))
                        visited.add((ne_x, ne_y))

            return -1

        # 3. 遍历拆除所有要拆除的树
        for i in range(len(forest_rank)):
            if i == 0:
                _, s1, s2 = 0, 0, 0  # 注意第一颗砍的树不在0, 0的情况
            else:
                _, s1, s2 = forest_rank[i - 1]
            _, e1, e2 = forest_rank[i]
            start = (s1, s2)
            end = (e1, e2)
            tmp_ans = bfs(forest, start, end)
            if tmp_ans < 0:
                return -1
            ans += tmp_ans
        return ans


test = Solution()
ret = test.cutOffTree([[4, 2, 3],
                       [0, 0, 1],
                       [7, 6, 5]])
print(ret)
