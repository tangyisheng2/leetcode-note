#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :258. Add Digits.py
# @Time      :3/2/22
# @Author    :Eason Tang


class Solution:
    def addDigits(self, num: int) -> int:
        """
        Simulation
        """
        while num >= 10:  # While the number contains 2 digit
            ans = 0  # Sotre the emp ans
            while num > 0:  # Update the temp ans
                ans += num % 10
                num //= 10
            num = ans  # Update the num, if the num >= 10, repeat
        return num

    def addDigits2(self, num: int) -> int:
        """
        Math
        :param num:
        :return:
        """
        return (num - 1) % 9 + 1 if num else 0
