#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :370. Range Addition.py
# @Time      :4/6/22
# @Author    :Eason Tang


class Solution:
    def solve(self, n, updates):
        ans = [0] * n
        for start, end, val in updates:
            ans[start] += val
            if end + 1 < len(ans):
                ans[end + 1] -= val
        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]
        return ans

    def getmostvisited2(self, n, sprints):
        ans = [0] * n
        for i in range(1, len(sprints)):
            start = min(sprints[i], sprints[i - 1])
            end = max(sprints[i], sprints[i - 1])
            val = 1
            ans[start] += val
            if end + 1 < len(ans):
                ans[end] -= val

        for i in range(1, len(ans)):
            ans[i] += ans[i - 1]

        return max(ans)


test = Solution()
ret = test.solve(5, [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
])
print(ret)

ret = test.getmostvisited(10, [2, 4, 1, 2])
print(ret)
