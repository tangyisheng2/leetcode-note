from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for index, num in enumerate(nums):
            if target - num in hashtable:
                return [index, hashtable[target-num]]
            else:
                hashtable[num] = index
        return []