#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :6135. Longest Cycle in a Graph.py
# @Time      :7/30/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def found_loop(node):
            nonlocal start
            if start:
                return

            if node in visited:
                start = node
                return

            visited.add(node)
            if edges[node] != -1:
                found_loop(edges[node])

        def get_loop_length(node, cur_len):
            if node in visited:
                nonlocal longest_ans
                longest_ans = cur_len
                return

            visited.add(node)

            if edges[node] != -1:
                get_loop_length(edges[node], cur_len + 1)

        visited = set()
        ans = -1

        start_arr = []
        for i in range(len(edges)):
            start = None
            visited = set()
            found_loop(i)
            if start:
                start_arr.append(start)

        for start in start_arr:  # 需要注意可能的不成环的情况，但是不能用not start判断，因为node可能为0
            visited = set()
            longest_ans = 0
            get_loop_length(start, 0)
            ans = max(ans, longest_ans)

        return ans


ret = Solution().longestCycle([2, -1, 3, 1])
