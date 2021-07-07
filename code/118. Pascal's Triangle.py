# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   118. Pascal's Triangle.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng

"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            tmp = [1 for _ in range(i + 1)]
            for j in range(1, len(tmp) - 1):
                # 在前两行这个for循环不会执行，因为range(1, 1不会触发)
                # ↓需要注意杨晖三角的行坐标是从1开始
                tmp[j] = res[i - 2][j - 1] + res[i - 2][j]
            res.append(tmp)

        return res

test = Solution()
test.generate(2)