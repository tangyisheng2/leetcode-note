#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :706. Design HashMap.py
# @Time      :5/20/22
# @Author    :Eason Tang


class MyHashMap(object):
    """
    使用数组套数组的方式实现哈希表。
    第一维数组是"桶"，每个桶指向其对应的列表。
    第二维数组是存储键值对item的列表，在读取时需要从前向后进行遍历，找到item[0] == key的元素并对其进行修改
    第三纬数组item包含两个元素：item[0] = key, item[1] = value
    """

    def __init__(self):
        self.buckets = 1009  # 分桶数一般取质数，这是因为经验上来说，质数个的分桶能让数据更加分散到各个桶中。
        # 下面的代码中把分桶数去了 1009，是因为 1009 是大于 1000 的第一个质数。
        self.hashmap = [[] for _ in range(self.buckets)]  # 构建第一维数组，每个第一维数组包含一个空的item列表

    def hash(self, key):
        return key % self.buckets  # 计算第一维数组中对应的key

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hashkey = self.hash(key)
        for item in self.hashmap[hashkey]:  # 对在item列表中的所有元素进行遍历并且修改
            if item[0] == key:
                item[1] = value
                return
        self.hashmap[hashkey].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hashkey = self.hash(key)
        for item in self.hashmap[hashkey]:
            if item[0] == key:
                return item[1]

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashkey = self.hash(key)
        for i, item in enumerate(self.hashmap[hashkey]):
            if item[0] == key:
                self.hashmap[hashkey].pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
