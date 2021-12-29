#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :1995. Count Special Quadruplets.py
# @Time      :12/28/21 5:15 PM
# @Author    :Eason Tang
from typing import List


class Solution:
    # https://leetcode-cn.com/problems/count-special-quadruplets/solution/tong-ji-te-shu-si-yuan-zu-by-leetcode-so-50e2/
    def countQuadruplets(self, nums: List[int]) -> int:
        """
        Brute Force
        Time: O(n^4)
        Space: O(1)
        """
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] == nums[l]:
                            ans += 1

        return ans

    def countQuadruplets2(self, nums: List[int]) -> int:
        """
        Use hashmap to storage nums[d]
        Time: O(n^3)
        Space: O(n)
        """
        import collections
        n = len(nums)
        ans = 0
        hashmap = collections.defaultdict(int)  # Create a empty dict to count the numbers that could be selected as d
        for c in range(n - 2, 1,
                       -1):  # start shrinking c from n - 2 (the last one is for d) to 2 (in this case, a = nums[0], b = nums[1])
            hashmap[nums[c + 1]] += 1  # update the dict with new range of d

            for a in range(c):
                for b in range(a + 1, c):
                    if (total := nums[a] + nums[b] + nums[c]) in hashmap:
                        # iterate through a and b and c, and check if d is in the dict
                        # PS: because we shrink the in reverse, so we can ensure that a < b < c < d
                        # Also, in case of multiple sum is presented in the nums, we add hashmap[total] to ans rather than 1
                        ans += hashmap[total]

        return ans

    def countQuadruplets3(self, nums: List[int]) -> int:
        """
        Use hashmap to storage nums[d] - nums[c], check if nums[a] + nums[b] = nums[c] + nums[d]
        Time: O(n^2)
        Space: O(2n)
        """
        import collections
        n = len(nums)
        ans = 0
        hashmap = collections.defaultdict(int)
        for b in range(n - 3, 0, -1):   # shrink b's range from n - 3 (c = n - 2, d = n - 1) to 1 (a = 0)
            for d in range(b + 2, n):   # iterate through every possible d from b + 2 (c = b + 1) to n and update the counter
                hashmap[nums[d] - nums[b + 1]] += 1
            for a in range(b):  # interate through every possible a and check result
                if (total := nums[a] + nums[b]) in hashmap:
                    ans += hashmap[total]

        return ans
