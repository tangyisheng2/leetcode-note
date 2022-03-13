#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :599. Minimum Index Sum of Two Lists.py
# @Time      :3/13/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_idx = len(list1) + len(list2)
        ans = []
        list1_idx = {}
        for i, name in enumerate(list1):
            list1_idx[name] = i

        for i, name in enumerate(list2):
            if name in list1_idx and i + list1_idx[name] < min_idx:
                min_idx = i + list1_idx[name]
                ans = [name]

            elif name in list1_idx and i + list1_idx[name] == min_idx:
                ans.append(name)

        return ans
