#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :57. Insert Interval.py
# @Time      :4/4/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        遍历intervals中的所有区间[l, r]
        三种情况：
        0. 原来的intervals为空
        1. r < newInterval[0]，说明[l, r]在newInterval的左边，没有交集，此时我们直接将原区间添加到答案
        2. newInterval[1] < l，说明[l, r]在newInterval的右边，没有交集，此时我们直接讲原区间添加到答案
        3. 除去以上两种情况，我们需要对新区建进行合并：
            新建一个区间讲所有需要合并的时间节点放进去，取其中的最小值和最大值合并成新的区间
        """
        ans = []
        merge_list = newInterval

        # Case 0
        if not intervals:
            return [newInterval]

        for l, r in intervals:
            # Case1
            if r < newInterval[0]:
                ans.append([l, r])
            # Case 2
            elif l > newInterval[1]:
                if merge_list:
                    ans.append(merge_list)
                    merge_list = []
                ans.append([l, r])
            else:
                merge_list[0] = min(merge_list[0], l)
                merge_list[1] = max(merge_list[1], r)

        # Corner Case： 如果原区间包含了新增区间（没有放置合并后的区间），将其添加到答案数组
        if merge_list:
            ans.append(merge_list)

        return ans
