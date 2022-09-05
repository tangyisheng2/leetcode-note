#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :937. Reorder Data in Log Files.py
# @Time      :9/4/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        import re
        letter_log = []
        number_log = []
        for i, log in enumerate(logs):
            log_arr = log.split(' ', 1)
            if re.search(r'[0-9]', log_arr[1]):
                number_log.append(i)
            else:
                letter_log.append(i)
        # print(letter_log)
        # print(number_log)
        letter_log.sort(key=lambda x: (logs[x].split(" ", 1)[1:], logs[x].split(" ", 1)[0]))
        # number_log.sort(key= lambda x: logs[x].split(" ", 1)[1:])

        return [logs[x] for x in [*letter_log, *number_log]]
