# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   8.2.2.Binary Straight Insertion Sort.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def binary_search(self, arr, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
        return left

    def insertion_sort(self, arr):
        n = len(arr)
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                insert_num = arr[i]  # 要插入的目标
                idx = self.binary_search(arr, 0, i - 1, insert_num)
                j = i - 1
                # 注意在排序的时候前面i个数已经排好了
                while j >= idx:  # 一直向前找，直到找到插入记录
                    arr[j + 1] = arr[j]  # 比插入元素大的元素都向后稍稍
                    j -= 1

                arr[idx] = insert_num  # 找到了第一个比插入元素小的元素，插在后面

        return arr


if __name__ == '__main__':
    ret = Solution().insertion_sort([2, 3, 1, 5])
    print(ret)
