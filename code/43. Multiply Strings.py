# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   43. Multiply Strings.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def multiply_w_digit(self, num1, num2, counter):
        """
        字符串与一位数字的乘法
        :param num1: 字符串1
        :param num2: 一位数字的字符串
        :param counter: 后面要补0的数量
        :return: 乘法结果
        """
        multiple_res = []
        carry = 0
        num2 = int(num2)
        for i in reversed(num1):
            res = int(i) * num2 + carry
            multiple_res.append(res % 10)
            carry = res // 10

        res = "".join([str(i) for i in reversed(multiple_res)])  # 数组转字符串
        res = res + "0" * counter  # 字符串后面补0
        if carry:
            res = str(carry) + res  # 补充carry位
        return res

    def string_add(self, num1, num2):
        """
        字符串相加
        :param num1: 字符串1
        :param num2: 字符串2
        :return: 相加结果
        """
        if len(num1) == 0:
            return num2
        if len(num2) == 0:
            return num1

        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res_stack = []
        while i >= 0 or j >= 0:
            num1_ = int(num1[i]) if i >= 0 else 0
            num2_ = int(num2[j]) if j >= 0 else 0

            res = num1_ + num2_ + carry
            res_stack.append(str(res % 10))
            carry = res // 10

            i -= 1
            j -= 1

        return "1" + "".join(reversed(res_stack)) if carry else "".join(reversed(res_stack))

    def multiply(self, num1: str, num2: str) -> str:
        """
        进行竖式加法主要分为两步：
        1. num2上每一位与num1相乘
        2. 将步骤1的结果进行加法，最后得到结果
        :param num1: num1数组
        :param num2: num2数组
        :return: 乘法结果
        """
        if num1 == "0" or num2 == "0":
            return "0"

        res = ""
        multiply_res_temp = []

        for i in reversed(range(len(num2))):
            counter = len(num2) - 1 - i
            res_tmp = self.multiply_w_digit(num1, num2[i], counter)
            multiply_res_temp.append(res_tmp)

        for i in range(len(multiply_res_temp)):
            res = self.string_add(res, multiply_res_temp[i])

        return res


test = Solution()
test.multiply(num1="123", num2="456")
