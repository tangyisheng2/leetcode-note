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
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k
            # 同余定理
            if presum in modes:
                return True
            # last是上一个元素的余数，presum是本次的余数
            modes.add(last)
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
