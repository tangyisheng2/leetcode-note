#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1010. Pairs of Songs With Total Durations Divisible by 60.py
# @Time      :6/20/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        使用二分查找的方式可以显著降低复杂度
        使用一个长度为60的数组存储余数的个数（注意当num为60的倍数时余数为0）
        对每一个数取余数，计算他的与60的互补个数并且添加到答案中
        更新余数数组
        :param time:
        :return:
        """
        remainder_cnt = [0] * 60
        ans = 0
        m = len(time)

        for i in range(m):
            num = time[i] % 60
            remainder = 60 - num
            if remainder == 60:
                ans += remainder_cnt[0]
            else:
                ans += remainder_cnt[remainder]

            remainder_cnt[num] += 1

        return ans


test = Solution()
ret = test.numPairsDivisibleBy60([60, 60, 60])
print(ret)
