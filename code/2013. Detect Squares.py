#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2013. Detect Squares.py
# @Time      :1/25/22
# @Author    :Eason Tang
from typing import List, Optional
import collections


class DetectSquares:

    def __init__(self):
        self.map = collections.defaultdict(collections.Counter)

    def add(self, point: List[int]) -> None:
        """
        使用哈希表 套 哈希表的方式存储
        外层哈希表的key为纵坐标y，value为内层哈希表
        内层哈希表的key为横坐标x，value为在[x, y]坐标点的点的个数
        :param point: [x, y]
        :return:
        """
        x, y = point
        self.map[y][x] += 1

    def count(self, point: List[int]) -> int:
        """
        给定顶点[x, y]，在map[y]中寻找其他已经存在的点，设已经存在的点坐标为[x1, y]，则正方形其中一条边为从[x, y]到[x1, y]，边长为x1 - x，设为d
        得到两点[x, y], [x1, y]以及长为d后，可知剩下的两点坐标为[x, y - d], [x1, y - d]
        如果在[x, y - d], [x1, y - d]两点的个数大于1，则使用乘法定理可得总共的四边形数量：
        [x, y], [x1, y], [x, y - d], [x1, y - d]
        [x, y], [x1, y], [x, y + d], [x1, y + d]
        :param point: 顶点[x, y]
        :return: 以顶点[x, y]组成的正方形数量
        """
        res = 0
        x, y = point

        if y not in self.map:  # 如果y在其纵坐标上没有点，则不能组成正方形
            return 0
        y_cnt = self.map[y]  # 纵坐标y上所有点的集合（类型为字典）

        for col, colCnt in self.map.items():
            # 遍历其他纵坐标=col的点
            if col != y:
                # 如果col = y，则面积为0，不能围成正方形
                # 根据对称性，这里可以不用取绝对值
                d = col - y
                """
                已知其中一个原点的坐标为[x, y], 其纵坐标为y，则我们遍历具有其他纵坐标col的点
                对于其他纵坐标col的点，可知正方形的边长d = col - y
                已知其中一个顶点坐标y和一条横边的纵坐标y1，可得可能存在正方形的两种点的集合：
                [x, y][x + d, y][x, col][x + d, col]
                [x, y][x - d, y][x, col][x - d, col]
                """
                #      [x, col]     [x + d, y]    [x + d, col]
                res += colCnt[x] * y_cnt[x + d] * colCnt[x + d]
                res += colCnt[x] * y_cnt[x - d] * colCnt[x - d]

        return res


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
obj.add([3, 10])
obj.add([11, 2])
obj.add([3, 2])
obj.count([11, 10])
obj.count([14, 8])
obj.add([11, 2])
obj.count([11, 10])
# param_2 = obj.count([11,2])
