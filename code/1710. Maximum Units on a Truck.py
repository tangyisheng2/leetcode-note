# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1710. Maximum Units on a Truck.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# class Solution:
#     def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
#         """
#         贪心
#         由于题目只对箱子的数量有限制，因此我们优先选择装unit多的箱子
#         同时需要注意判断两个特殊情况：
#         1. 一类箱子没有完全装完的时候已经到达truckSize
#         2. 全部箱子装完仍没有到达truckSize
#         :param boxTypes: [箱子个数, 箱子所装的Unit数]
#         :param truckSize: 最大的truck数量
#         :return: 最大能装的unit
#         """
#         count = [i[0] for i in boxTypes]
#         units = [i[1] for i in boxTypes]
#         box_count = 0
#         ans = 0
#
#         while box_count < truckSize and units:
#             sel_idx = units.index(max(units))
#             box_to_load = min(count[sel_idx], truckSize - box_count)
#             box_count += box_to_load
#             ans += units[sel_idx] * box_to_load
#
#             count.pop(sel_idx)
#             units.pop(sel_idx)
#
#         return ans

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        优化版本
        :param boxTypes:
        :param truckSize:
        :return:
        """
        boxTypes = sorted(boxTypes, key=lambda x: x[1])  # 按照boxTypes第二个元素进行升序排序
        box_count = 0
        ans = 0
        while boxTypes and box_count < truckSize:  # 当box不为空并且还没有到达truckSize的上限
            box_num, unit_num = boxTypes.pop()  # 选取下一类unit最多的box
            box_count_to_load = min(box_num, truckSize - box_count)  # 计算能装的box数量（取决于1. 该类box的数量，2. truck上的可用空间的最小值）
            box_count += box_count_to_load  # 更新已装box数
            ans += box_count_to_load * unit_num  # 更新已装unit数
        return ans


test = Solution()
test.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4)
