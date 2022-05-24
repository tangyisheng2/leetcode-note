#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :179. Largest Number.py
# @Time      :5/24/22
# @Author    :Eason Tang
import functools
from typing import List


class Solution(object):
    def largestNumber(self, nums):
        """
        第一步：定义比较函数，把最大的放左边
        第二步：排序
        第三步：返回结果
        :type nums: List[int]
        :rtype: str
        """

        def compare(x, y):
            """
            将 xy 与 yx 比较大小
            :param x:
            :param y:
            :return:
            """
            return int(y + x) - int(x + y)

        nums = sorted(map(str, nums), key=functools.cmp_to_key(compare))
        # map(func, arr): 对arr中的每一个元素调用func函数，返回生成的新arr
        # functools.cmp_to_key(compare_func) 将compare_func对比的结果转换为key进行排序
        return "0" if nums[0] == "0" else "".join(nums)
        # 如果最高位已经是0，则所有的其他数字也会是0，直接返回"0"
