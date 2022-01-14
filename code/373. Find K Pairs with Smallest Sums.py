#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :373. Find K Pairs with Smallest Sums.py
# @Time      :1/13/22
# @Author    :Eason Tang
from typing import List, Optional
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/solution/tong-ge-lai-shua-ti-la-you-xian-ji-dui-l-fw7y/
        先把所有的 nums1 的索引入队，即入队的元素有 [0, 0]、[1, 0]、[2, 0]、[3, 0]、......
        首次弹出的肯定是 [0, 0]，再把 [0, 1] 入队；
        这样就可以通过优先级队列比较 [0, 1] 和 [1, 0] 的结果，再弹出较小者；
        依次进行，进行 k 轮。

        :param nums1:
        :param nums2:
        :param k:
        :return:
        """
        m, n = len(nums1), len(nums2)
        ans = []
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        while pq and len(ans) < k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
        return ans


test = Solution()
test.kSmallestPairs(nums1=[1, 1, 2, 3], nums2=[1, 2, 3], k=2)
