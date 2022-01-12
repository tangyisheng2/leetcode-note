#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :306. Additive Number.py
# @Time      :1/9/22 11:05 PM
# @Author    :Eason Tang
import math


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(p, q):
            last, first, second = 0, p, q
            while second < len(num):
                if (num[last] == '0' and first > last + 1) or (num[first] == '0' and second > first + 1):
                    return False
                s = int(num[last:first]) - int(num[first:second])
                # if num[second:second + len(s)] != s:
                if int(num[second: second + math.log10(s)]) != s:
                    return False
                last, first, second = first, second, second + len(s)
            return True

        for i in range(1, len(num) - 1):
            for j in range(i + 1, len(num)):
                if dfs(i, j):
                    return True
        return False

test = Solution()
test.isAdditiveNumber("112358")