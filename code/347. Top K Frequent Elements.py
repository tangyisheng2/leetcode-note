#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :347. Top K Frequent Elements.py
# @Time      :12/20/21 11:56 AM
# @Author    :Eason Tang
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        ans = []
        frequency = collections.Counter(nums)
        frequency_reverse = [(v, k) for k, v in frequency.items()]  # Reverse the key and value
        frequency_reverse.sort()
        for i in range(1, k + 1):
            ans.append(frequency_reverse[-i][1])
        return ans

test = Solution()
print(test.topKFrequent([1,1,1,2,2,3], 2))