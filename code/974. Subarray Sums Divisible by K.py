# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   974. Subarray Sums Divisible by K.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import collections
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0  # 前缀和
        ans = 0
        prefix_mod = {0: 1} # 
        for i in range(len(nums)):
            prefix_sum += nums[i]  # 逐次相加，如果用sum会超时
            mod_result = prefix_sum % k
            if mod_result not in prefix_mod:  # 如果dict中不存在记录则要新建
                prefix_mod[mod_result] = 0
            ans += prefix_mod[mod_result]  # 当dict中相同前缀和有k个的时候，第i个前缀和可以和前面已经存在的k个前缀和组成k个新的子数组
            prefix_mod[mod_result] += 1  # 更新前缀和记录
        return ans


test = Solution()
ret = test.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5)
print(ret)
