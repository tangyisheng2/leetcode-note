#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :969. Pancake Sorting.py
# @Time      :2/18/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for n in range(len(arr), 1, -1):
            index = 0
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            if index == n - 1:
                continue
            m = index  # 反转的半径为index
            # for i in range(math.ceil(m / 2)):
            for i in range((m + 1) // 2):
                # 原地反转时，我们对半径为(m + 1) // 2的元素与另一半边进行反转
                arr[i], arr[m - i] = arr[m - i], arr[i]  # 原地反转
            for i in range(n // 2):
                # 在进行过一次的反转后，我们在进行下一次反转即可以将想要的元素放到最末尾的位置
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]  # 原地反转
            ans.append(index + 1)  # 添加第一次旋转的半径到ans
            ans.append(n)  # 添加第二次旋转的半径到ans
        return ans


test = Solution()
ret = test.pancakeSort([3, 2, 4, 1])
