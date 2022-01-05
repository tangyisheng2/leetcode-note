#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :390. Elimination Game.py
# @Time      :1/1/22 10:02 PM
# @Author    :Eason Tang
"""
Eliminate 3
Round \ Index	0	1	2	3	4	5	6	7	8	9	10
            1	1	2	3	4	5	6	7	8	9	10	11
            2	4	5	6	7	8	9	10	11	1	2
            3	7	8	9	10	11	1	2	4	5
            4	10	11	1	2	4	5	7	8
            5	2	4	5	7	8	10	11
            6	7	8	10	11	2	4
            7	11	2	4	7	8
            8	7	8	11	2
            9	2	7	8
            10	2	7
            11	7
            约瑟夫环
"""
class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left = True

        while n > 1:
            # 从左边开始移除 or（从右边开始移除，数列总数为奇数）
            if left or n % 2 != 0:
                head += step

            step <<= 1  # 步长 * 2
            n >>= 1  # 总数 / 2
            left = not left  # 取反移除方向

        return head