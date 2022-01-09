#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1629. Slowest Key.py
# @Time      :1/8/22 9:38 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        """
        We track the maximum key and value while iterating through the list
        """
        import collections
        pressed_time = collections.defaultdict(int)
        max_pressed_time = 0
        max_pressed_key = chr(0)
        for i in range(len(releaseTimes)):
            if i == 0:  # For the first element, just update the max_key and max_time
                pressed_time[keysPressed[0]] = releaseTimes[0]
                max_pressed_time = releaseTimes[0]
                max_pressed_key = keysPressed[0]
            elif (pressed_time := releaseTimes[i] - releaseTimes[i - 1]) >= max_pressed_time:
                # If found bigger key, update the max_key and max_time
                if pressed_time == max_pressed_time:    # If the time is the same, we just update the key
                    max_pressed_key = max(max_pressed_key, keysPressed[i])
                else:   # else update the time and key
                    max_pressed_key = keysPressed[i]
                    max_pressed_time = pressed_time
        return max_pressed_key

