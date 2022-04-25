#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :398. Random Pick Index.py
# @Time      :4/24/22
# @Author    :Eason Tang
from typing import List


class Solution2:
    def __init__(self, nums: List[int]):
        import collections
        self.pos = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.pos[num].append(i)

    def pick(self, target: int) -> int:
        import random
        return random.choice(self.pos[target])


class Solution1:
    """
    水塘抽样：Reservoir sampling
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        import random
        ans = 0
        cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if random.randrange(cnt) == 0:
                    ans = i
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
