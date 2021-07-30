# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   8.2.2.Binary Straight Insertion Sort.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def shell_s_sort(self, arr, dk):
        n = len(arr)
        for i in range(1, n - dk):
            insert_num = arr[i]  # 要插入的目标
            j = i - 1
            # 注意在排序的时候前面i个数已经排好了
            while j >= 0 and insert_num < arr[j]:  # 一直向前找，直到找到插入记录
                arr[j + dk] = arr[j]  # 比插入元素大的元素都向后稍稍
                j -= dk
            j += dk  # 在上一行我们的j多减了1
            arr[j] = insert_num  # 找到了第一个比插入元素小的元素，插在后面

        return arr


if __name__ == '__main__':
    arr = [2, 3, 1, 5]
    for i in range(len(arr)):
        arr = Solution().shell_s_sort(arr, i)
    print(arr)
