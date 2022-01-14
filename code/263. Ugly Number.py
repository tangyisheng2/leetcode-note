#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :263. Ugly Number.py
# @Time      :1/13/22
# @Author    :Eason Tang
from typing import List, Optional


class Solution:
    def isUgly(self, n: int) -> bool:
        """
        We divide n with factor 2, 3, 5.
        If the remainder is not 1, there will be another factor
        :param n:
        :return:
        """
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n /= factor

        return n == 1
