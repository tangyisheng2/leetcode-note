# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   442. Find All Duplicates in an Array.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def findDuplicates(self, nums: List[int]) -> List[int]:
#         """
#         用set进行去重
#         :param nums: 输入array
#         :return: 数组中出现两次的元素array
#         """
#         temp = set()
#         ans = []
#         for num in nums:
#             if num in temp:
#                 ans.append(num)
#             temp.add(num)
#         return ans

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        观察到constrain中n == nums.length，同时1 <= nums[i] <= n
        假设x = nums[i]
        我们可以使用nums[x - 1]的正负来判断x这个数字是否出现两次
        注意：由于直接使用x作为索引可能会越界，所以我们使用x - 1来避免越界问题（）
        :param nums:
        :return:
        """
        ans = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:  # 使用num - 1作为索引避免越界
                ans.append(abs(num))
            nums[num - 1] = -nums[num - 1]
        return ans
