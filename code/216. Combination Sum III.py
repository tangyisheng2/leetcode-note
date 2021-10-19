#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :216. Combination Sum III.py
# @Time      :10/18/21 10:58 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(target, digit_count, begin_idx, current_state, ans):
            if digit_count == 0:
                if target == 0:
                    ans.append(current_state[:])
                return

            for i in range(begin_idx, 10):
                if i > target:
                    return

                current_state.append(i)
                dfs(target - i, digit_count - 1, i + 1, current_state, ans)
                current_state.pop()

        ans = []
        dfs(n, k, 1, [], ans)
        return ans


test = Solution()
test.combinationSum3(k=3, n=9)
