#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1.py
# @Time      :9/26/21 8:28 PM
# @Author    :Eason Tang
def firstNotRepeatingCharacter(s):
    if len(set(s)) == len(s):  # 没有重复
        return s[0]

    n = len(s)
    dup = set()
    for i in range(n):
        if s[i] not in dup:  # i不在重复
            for j in range(i + 1, n):  # j寻找重复
                if s[i] == s[j]:  # 如果找到重复的数值
                    dup.add(s[i])
                    break
                if j == n - 1:
                    return s[i]


firstNotRepeatingCharacter("abacabad")


import math
math.log