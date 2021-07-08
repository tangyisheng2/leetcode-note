# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   523. Continuous Subarray Sum.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         """
#         brute force
#         :param nums:
#         :param k:
#         :return:
#         """
#         for lo in range(len(nums)):
#             for hi in range(lo, len(nums)):
#                 if len(nums[lo:hi + 1]) >= 2 and sum(nums[lo:hi + 1]) % k == 0:
#                     return True
#         return False

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        mod_mark = {0: -1}  # 规定 空的前缀的结束下标为−1，由于 空的前缀的 元素和为0，因此在哈希表中存入键值对(0,−1)。
        mod = 0
        for i in range(n):
            mod = (mod + nums[i]) % k
            if mod in mod_mark:
                if i - mod_mark[mod] >= 2:
                    return True
            else:
                mod_mark[mod] = i
        return False


test = Solution()
ret = test.checkSubarraySum([2, 4, 3], 6)
print(ret)

# [23,2,4,6,7]
# 6
# [23,2,6,4,7]
# 6
# [23,2,6,4,7]
# 13
# [0]
# 1
# [1,0]
# 2
# [23,2,4,6,6]
# 7
# [0,0]
# 1
# [23,6,9]
# 6
# [1]
# 1
# [2,4,3]
# 6
