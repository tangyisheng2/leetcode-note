#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :767. Reorganize String.py
# @Time      :5/28/22
# @Author    :Eason Tang


class Solution:
    def reorganizeString(self, s: str) -> str:
        import collections
        import heapq
        cnt = collections.Counter(s)
        n = len(s)
        ans = []

        # Check if it is possible to construct the string
        maxCount = max(cnt.items(), key=lambda x: x[1])[1]
        if maxCount > (n + 1) // 2:
            return ""

        # Construct max heap
        heap = [(-x[1], x[0]) for x in cnt.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            # 注意此处是大根堆，cnt1和cnt2是负数，下面更新cnt1和cnt2的时候应该+=1
            cnt1, ch1 = heapq.heappop(heap)
            cnt2, ch2 = heapq.heappop(heap)

            ans.extend([ch1, ch2])

            #
            cnt1 += 1
            cnt2 += 1

            if cnt1 < 0:
                heapq.heappush(heap, (cnt1, ch1))

            if cnt2 < 0:
                heapq.heappush(heap, (cnt2, ch2))

            if len(heap) == 1:
                ans.append(heapq.heappop(heap)[1])

        return "".join(ans)


test = Solution()
ret = test.reorganizeString("aab")
