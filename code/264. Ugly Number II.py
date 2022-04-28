#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :264. Ugly Number II.py
# @Time      :1/14/22
# @Author    :Eason Tang


# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         if n == 1:
#             return 1
#         factor_2 = [2 * x for x in range(n)]
#         factor_3 = [3 * x for x in range(n)]
#         factor_5 = [5 * x for x in range(n)]
#         ptr_2, ptr_3, ptr_5 = 1, 1, 1
#         ans = [1]
#
#         while len(ans) < n:
#             min_number = min(factor_2[ptr_2], factor_3[ptr_3], factor_5[ptr_5])
#             if min_number % 2 == 0:
#                 ans.append(factor_2[ptr_2])
#                 ptr_2 += 1
#             if min_number % 3 == 0:
#                 ans.append(factor_3[ptr_3])
#                 ptr_3 += 1
#             if min_number % 5 == 0:
#                 ans.append(factor_5[ptr_5])
#                 ptr_5 += 1
#
#         return ans
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [0, 1]
        i2 = 1
        i3 = 1
        i5 = 1
        for idx in range(2, n + 1):
            a = ans[i2] * 2
            b = ans[i3] * 3
            c = ans[i5] * 5
            min_number = min([a, b, c])

            if min == a:
                i2 += 1
            if min == b:
                i3 += 1
            if min == c:
                i5 += 1
            ans.append(min)
        return ans[n]


test = Solution()
test.nthUglyNumber(10)
