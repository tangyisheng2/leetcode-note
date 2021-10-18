#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :40. Combination Sum II.py
# @Time      :10/17/21 11:45 PM
# @Author    :Eason Tang
from typing import List


# https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start_idx, current_state, ans):
            if target == 0:
                ans.append(current_state[:])
                return

            for i in range(start_idx, len(candidates)):
                if candidates[start_idx] > target:
                    return
                if i > start_idx and candidates[i - 1] == candidates[i]:
                    continue

                remainder_target = target - candidates[i]
                current_state.append(candidates[i])
                dfs(candidates, remainder_target, i + 1, current_state, ans)
                current_state.pop()

        candidates.sort()
        ans = []
        dfs(candidates, target, 0, [], ans)
        return ans

# class Solution:
#
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         def dfs(candidates, target, start_idx, path, ans):
#             if target == 0:
#                 ans.append(path[:])
#                 return
#
#             for index in range(start_idx, size):
#                 if candidates[index] > target:
#                     break
#
#                 if index > start_idx and candidates[index - 1] == candidates[index]:
#                     continue
#
#                 path.append(candidates[index])
#                 dfs(candidates, target - candidates[index], index + 1, path, ans)
#                 path.pop()
#
#         size = len(candidates)
#         if size == 0:
#             return []
#
#         candidates.sort()
#         ans = []
#         dfs(candidates, target, 0, [], ans)
#         return ans


test = Solution()
print(test.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
