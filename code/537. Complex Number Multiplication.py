#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :537. Complex Number Multiplication.py
# @Time      :2/24/22
# @Author    :Eason Tang
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        """
        let num1 = a+bi
            num2 = c+di
        3 type:
        1. 1+j0 * 1+j0
        2. 1+j0 * 1+j1
        3. 1+j1 * 1+j1
        """
        num1 = num1.split("+")
        num2 = num2.split("+")
        a = int(num1[0])
        b = int(num1[1][:-1])
        c = int(num2[0])
        d = int(num2[1][:-1])
        return f'{a * c - b * d}+{b * c + a * d}i'
