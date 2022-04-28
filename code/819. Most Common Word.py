#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :819. Most Common Word.py
# @Time      :4/16/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        注意：
        1. paragraph包括大小写英文字母，但是返回值需要为小写字母，首先我们使用.lower()方法将其变成全小写
        2. paragraph中包含两种分隔符，其中包括标点"!?',;."和空格" "
        不能直接将标点去除并且按照空格分割（例外情况：a,b,c d, e）
        而应该将标点替换成空格并且按照空格分割（多个空格会当作一个分割点进行处理）
        Tips: 如何对对个标点富豪进行快速替换：使用正则表达式
        re.sub("[!?',;.]", " ", paragraph.lower()).split()
        [!?',;.] 代表替换其中的任意一个字符
        " " 代表替换为空格
        paragraph.lower() 欲替换的字符串是原paragraph的小写
        .split() 分割字符串
        :param paragraph:
        :param banned:
        :return:
        """
        import collections
        import re
        banned = set([word.lower() for word in banned])
        cnt = collections.defaultdict(int)

        word_list = re.sub("[!?',;.]", " ", paragraph.lower()).split()
        ans_cnt = 0
        ans = None

        for word in word_list:
            if word not in banned:
                cnt[word] += 1

                if ans is None or cnt[word] > ans_cnt:
                    ans_cnt = cnt[word]
                    ans = word

        return ans
