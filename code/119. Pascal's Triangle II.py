# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   119. Pascal's Triangle II.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng

@Modify Time        @Author     @Version        @Description
------------        -------     --------        -----------
2021/7/7     tangyisheng2        1.0             数据库链接
"""
from typing import List


# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         """
#         原始版本
#         :param rowIndex:
#         :return:
#         """
#         res = []
#         n_row = rowIndex + 2
#         for i in range(1, n_row):
#             tmp = [1 for _ in range(i)]
#             for j in range(1, len(tmp) - 1):
#                 tmp[j] = res[i - 2][j - 1] + res[i - 2][j]
#             res.append(tmp)
#
#         return res[rowIndex]

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        空间优化，仅保留最后两行
        :param rowIndex:
        :return:
        """
        res = []
        for i in range(rowIndex + 1):
            tmp = [1 for _ in range(i + 1)]  # 我们的index从0算起，所以要加1
            for j in range(1, len(tmp) - 1):
                tmp[j] = res[1][j - 1] + res[1][j]
            res.append(tmp)
            if i > 1:
                res.pop(0)

        return res[-1]


test = Solution()
test.getRow(3)
