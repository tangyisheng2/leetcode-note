# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   47. Permutations II.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def dfs(self, prefix, cnt, visit_hist, nums, ans):
        if prefix is not None and len(prefix) == len(nums):
            ans.append(prefix[:])

        for i in range(cnt, len(nums)):
            if visit_hist[i] or i > 0 and nums[i] == nums[i - 1] and not visit_hist[i - 1]:
                continue
            prefix.append(nums[i])
            visit_hist.append(nums[i])
            self.dfs(prefix, cnt + 1, visit_hist, nums, ans)
            prefix.pop()
            visit_hist.pop()
        return ans

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        return self.dfs([], 0, [0], nums, ans)


if __name__ == '__main__':
    test = Solution()
    test.permuteUnique(nums=[1, 1, 2])
