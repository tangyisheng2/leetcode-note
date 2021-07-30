# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   8.4.1 Simple Selection Sort.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] < arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = tmp
        return arr


if __name__ == '__main__':
    ret = Solution().sort([2, 3, 1, 5])
    print(ret)
