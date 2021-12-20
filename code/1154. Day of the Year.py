#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1154. Day of the Year.py
# @Time      :12/20/21 11:52 AM
# @Author    :Eason Tang
class Solution:
    def dayOfYear(self, date: str) -> int:
        ans = 0
        date_arr = [int(i) for i in date.split("-")]
        print(date_arr)
        is_leap_year = (date_arr[0] % 4 == 0 and date_arr[0] % 100 != 0) or (
                    date_arr[0] % 100 == 0 and date_arr[0] % 400 == 0)
        normal_year_day_count = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap_year_day_count = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(date_arr[1] - 1):
            if is_leap_year:
                ans += leap_year_day_count[i]
            else:
                ans += normal_year_day_count[i]

        ans += date_arr[2]
        return ans
