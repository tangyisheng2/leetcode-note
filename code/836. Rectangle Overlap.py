# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   836. Rectangle Overlap.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        0: left boarder
        1: bottom boarder
        2: right boarder
        3: top boarder
        """

        return not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
