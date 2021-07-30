# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   8.3.2 Quick Sort.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
import random


class Solution:
    def quick_sort(self, nums, low, hi):
        """

        :param nums:
        :param low:
        :param hi:
        :return:
        """
        i, j = low, hi
        if i >= j:  # 如果low大于hi，则所有元素都已排序完成
            return nums

        pivot = nums[i]  # 选择第一个元素作为pivot

        while i < j:
            while i < j and nums[j] >= pivot:  # 从右向左找到第一个比pivot小的元素
                j -= 1
            nums[i] = nums[j]  # 将j放到i上（j空出来）
            while i < j and nums[i] <= pivot:  # 从左向右找到第一个比pivot大的元素
                i += 1
            nums[j] = nums[i]  # 将i放到j上（i空出来）
        nums[i] = pivot  # 交换pivot（此时i = j所以其实无所谓）
        self.quick_sort(nums, low, i - 1)
        self.quick_sort(nums, i + 1, hi)
        return nums


if __name__ == '__main__':
    ret = Solution().quick_sort([random.randint(0, 100) for _ in range(100)], 0, 99)
    print(ret)
