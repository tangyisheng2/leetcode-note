# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   78. Subsets.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dp = [[[]] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(len(dp[i - 1])):
                dp[i] = dp[i - 1]   # 先将之前的结果复制一份
                if not dp[i - 1][j]:  # 增加元素
                    dp[i].append([nums[i - 1]])
                else:
                    dp[i].append(dp[i - 1][j] + [nums[i - 1]])
        return dp[-1]


# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         n = len(nums)
#
#         def helper(i, path):
#             res.append(path)
#             for j in range(i, n):
#                 helper(j + 1, path + [nums[j]])
#
#         helper(0, [])
#         return res


if __name__ == '__main__':
    ret = Solution().subsets([1, 2, 3])