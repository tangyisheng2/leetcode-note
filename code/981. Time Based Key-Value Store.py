#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :981. Time Based Key-Value Store.py
# @Time      :11/5/21 11:13 AM
# @Author    :Eason Tang
class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        if key in self.dict:
            self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dict:
            nums = self.dict[key]
            target = timestamp
            idx = self.binarysearch(nums, target)
            return self.dict[key][idx][1] if idx >= 0 else ""
        return ""

    def binarysearch(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid][0] > target:
                hi = mid - 1
            elif nums[mid][0] < target:
                lo = mid + 1
            else:
                return mid
        return hi


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
obj = TimeMap()
obj.set("love", "high", 10)
obj.set("love", "low", 20)
param_3 = obj.get("love", 5)
param_3 = obj.get("love", 15)
print(param_3)
