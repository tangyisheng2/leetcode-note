#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Recursive_4. Towers of Hanoi.py
# @Time      :12/24/21 11:48 AM
# @Author    :Eason Tang
def hanoi(n, x, y, z):
    """
    This function moves n plate from x to y using z
    :param n: number of plate
    :param x: start post
    :param y: destination post
    :param z: helper post
    :return:
    """
    if n == 1:
        print(x, '->', y)  # 当只有一个在A时，将唯一的（也是最大的）一个从A移到B
    else:
        hanoi(n - 1, x, z, y)  # 将除了最大以外的所有盘子移到第三根柱子（helper post）上
        print(x, '->', y)  # 打印移动的步骤
        hanoi(n - 1, z, y, x)  # 将除了最大以外的所有盘子移回第二根柱子（helper post）上


hanoi(3, 'A', 'B', 'C')
