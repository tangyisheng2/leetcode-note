#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2038. Remove Colored Pieces if Both Neighbors are the Same Color.py
# @Time      :3/21/22
# @Author    :Eason Tang


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """
        We check teh consecutive colors, the one have more color wins:
        Use A_cnt and B_cnt to count the colors
        eg:
        For AAA, A_cnt += 2
            AAAA, A_cnt = 3
        """
        if not colors:
            return False
        ans_cnt = {"A": 0, "B": 0}  # [Alice, Bob]
        colors = list(colors)
        ptr = 1
        last_color = colors[0]
        cur_color_cnt = 1

        while ptr < len(colors):
            if colors[ptr] == last_color:
                cur_color_cnt += 1
                if cur_color_cnt >= 3:
                    ans_cnt[colors[ptr]] += 1
            else:
                last_color = colors[ptr]
                cur_color_cnt = 1
            ptr += 1

        return ans_cnt["A"] > ans_cnt["B"]
