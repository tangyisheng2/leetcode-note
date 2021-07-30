# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   8.2.1.Straight Insertion Sort.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            insert_num = arr[i]  # 要插入的目标
            j = i - 1
            # 注意在排序的时候前面i个数已经排好了
            while j >= 0 and insert_num < arr[j]:  # 一直向前找，直到找到插入记录
                arr[j + 1] = arr[j]  # 比插入元素大的元素都向后稍稍
                j -= 1
            j += 1  # 在上一行我们的j多减了
            arr[j] = insert_num  # 找到了第一个比插入元素小的元素，插在后面

        return arr


if __name__ == '__main__':
    ret = Solution().insertion_sort([2, 3, 1, 5])
    print(ret)
