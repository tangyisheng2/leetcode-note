# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   47. Permutations II.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


# https://leetcode-cn.com/problems/permutations-ii/solution/hot-100-47quan-pai-lie-ii-python3-hui-su-kao-lu-zh/
# https://leetcode-cn.com/problems/permutations-ii/solution/quan-pai-lie-ii-by-leetcode-solution/
# class Solution:
#     def dfs(self, prefix, cnt, visit_hist, nums, ans):
#         if prefix is not None and len(prefix) == len(nums):
#             ans.append(prefix[:])
#
#         for i in range(cnt, len(nums)):
#             if visit_hist[i] or i > 0 and nums[i] == nums[i - 1] and not visit_hist[i - 1]:
#                 """要解决重复问题，我们只要设定一个规则，保证在填第 \textit{idx}idx
#                 个数的时候重复数字只会被填入一次即可。而在本题解中，我们选择对原数组排序，保证相同的数字都相邻，然后每次填入的数一定是这
#                 个数所在重复数集合中「从左往右第一个未被填过的数字」，即如下的判断条件：
#                 这个判断条件保证了对于重复数的集合，一定是从左往右逐个填入的。
#
#                 假设我们有 3 个重复数排完序后相邻，那么我们一定保证每次都是拿从左往右第一个未被填过的数字，
#                 即整个数组的状态其实是保证了 [未填入，未填入，未填入] 到 [填入，未填入，未填入]，再到 [
#                 填入，填入，未填入]，最后到 [填入，填入，填入] 的过程的，因此可以达到去重的目标。
#
#                 """
#                 continue
#             prefix.append(nums[i])
#             visit_hist.append(nums[i])
#             self.dfs(prefix, cnt + 1, visit_hist, nums, ans)
#             prefix.pop()
#             visit_hist.pop()
#         return ans
#
#     def permuteUnique(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         return self.dfs([], 0, [0], nums, ans)

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, visited, current_stat, ans):
            if len(current_stat) == len(nums):
                ans.append(current_stat[:])

            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    """要解决重复问题，我们只要设定一个规则，保证在填第 \textit{idx}idx 
                    个数的时候重复数字只会被填入一次即可。而在本题解中，我们选择对原数组排序，保证相同的数字都相邻，然后每次填入的数一定是这
                    个数所在重复数集合中「从左往右第一个未被填过的数字」，即如下的判断条件： 
                    这个判断条件保证了对于重复数的集合，一定是从左往右逐个填入的。 

                    假设我们有 3 个重复数排完序后相邻，那么我们一定保证每次都是拿从左往右第一个未被填过的数字，
                    即整个数组的状态其实是保证了 [未填入，未填入，未填入] 到 [填入，未填入，未填入]，再到 [
                    填入，填入，未填入]，最后到 [填入，填入，填入] 的过程的，因此可以达到去重的目标。 

                    """
                    continue

                current_stat.append(nums[i])
                visited[i] = True
                dfs(nums, visited, current_stat, ans)
                current_stat.pop()
                visited[i] = False

            return ans

        nums.sort()
        ans = []
        return dfs(nums, [False] * len(nums), [], ans)


if __name__ == '__main__':
    test = Solution()
    test.permuteUnique(nums=[1, 1, 2])
