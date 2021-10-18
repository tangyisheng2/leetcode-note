#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :77. Combinations.py
# @Time      :10/18/21 12:21 AM
# @Author    :Eason Tang
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(candidates, solved_number, begin_idx, current_stat, sum_set, ans):
            current_sum = sum(current_stat)
            if solved_number == k:
                ans.append(current_stat[:])
                sum_set.add(current_sum)
                return

            for i in range(begin_idx, len(candidates)):
                current_stat.append(candidates[i])
                dfs(candidates, solved_number + 1, i + 1, current_stat, sum_set, ans)
                current_stat.pop()

        candidates = [i for i in range(1, n + 1)]
        sum_set = set()
        ans = []
        dfs(candidates, 0, 0, [], sum_set, ans)
        return ans


test = Solution()
res = test.combine(4, 2)
print(res)
