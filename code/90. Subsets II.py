#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :90. Subsets II.py
# @Time      :10/18/21 10:50 PM
# @Author    :Eason Tang
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, solved_number, begin_idx, current_stat, ans):
            ans.append(current_stat[:])

            for i in range(begin_idx, len(nums)):
                if i > begin_idx and nums[i] == nums[i - 1]:
                    continue
                current_stat.append(nums[i])
                dfs(nums, solved_number + 1, i + 1, current_stat, ans)
                current_stat.pop()
        nums.sort()
        ans = []
        dfs(nums, 0, 0, [], ans)
        return ans
