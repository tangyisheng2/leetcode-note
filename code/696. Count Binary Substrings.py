#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :696. Count Binary Substrings.py
# @Time      :2021/6/22 3:58 PM
# @Author    :Eason Tang

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        将字符串s按照0和1的连续段进行分组，并且将每一个分组中的数字个数存放在数组中
        这样的话数组前后的数字就一定是不同的0和1
        只要计算每组相邻的0和1对最后答案的贡献就可以得出答案
        """
        count = []  # 存放分组个数
        ptr = 0  # 指针
        while ptr < len(s):  # 指针右移
            temp_count = 0  # 每一个分组的临时计数
            ch = s[ptr]  # 记录这个分组的字符
            while ptr < len(s) and s[ptr] == ch:  # 如果指针没有达到末尾而且字符没有变
                ptr += 1
                temp_count += 1  # 临时分组+1
            count.append(temp_count)  # 结果数组增加
        ret = 0
        for i in range(1, len(count)):
            ret += min(count[i - 1], count[i])
        return ret


test = Solution()
ret = test.countBinarySubstrings(s="00110011")
print(ret)
