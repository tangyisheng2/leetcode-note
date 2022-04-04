#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :762. Prime Number of Set Bits in Binary Representation.py
# @Time      :4/4/22
# @Author    :Eason Tang
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        """
        10e6最多有23bit，先预处理出从2到23的prime number（1不是prime number）
        然后使用bit_count()计算有多少个二进制1
        """
        prime_number_set = {2, 3, 5, 7, 11, 13, 17, 19, 23}
        ans = 0
        for i in range(left, right + 1):
            if i.bit_count() in prime_number_set:
                ans += 1
        return ans
