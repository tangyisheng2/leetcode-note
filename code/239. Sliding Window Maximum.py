#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :239. Sliding Window Maximum.py
# @Time      :10/13/21 12:04 AM
# @Author    :Eason Tang

from typing import List


class Solution:
    """
        作者：LeetCode - Solution
        链接：https: // leetcode - cn.com / problems / sliding - window - maximum / solution / hua - dong - chuang - kou - zui - da - zhi - by - leetco - ki6m /
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        n = len(nums)
        max_queue = collections.deque()  # 单调队列，从头到尾单调递减，在这里我们存放idx

        for i in range(k):  # 针对第一个窗口的k个元素构建单调队列
            while max_queue and nums[i] >= nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(i)

        ans = [nums[max_queue[0]]]  # 第一个滑动窗口的最大值

        for i in range(k, n):  # 对后面窗口的元素构建队列
            while max_queue and nums[i] >= nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(i)

            while nums[max_queue[0]] <= i - k:
                """
                此时的最大值可能在滑动窗口左边界的左侧，并且随着窗口向右移动，它永远不可能出现在滑动窗口中了。因此我们还需要不断从队首弹出元素，直到队首元素在窗口中为止。
                """
                max_queue.popleft()
            ans.append(nums[max_queue[0]])

        return ans
