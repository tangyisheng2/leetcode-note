"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:
Input: candidates = [2], target = 1
Output: []
Example 4:
Input: candidates = [1], target = 1
Output: [[1]]
Example 5:
Input: candidates = [1], target = 2
Output: [[1,1]]

Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
from typing import List

# class Solution:
#     memo = {}
#
#     def combinationSum(self, candidates, target: int):
#         """
#         canSum
#         :param candidates:
#         :param target:
#         :return:
#         """
#         if target in self.memo:
#             return self.memo[target]
#         if target == 0:  # basecase: 0无论有没有candidate都能组成，返回true
#             return True
#         if target < 0:
#             return False
#         for num in candidates:
#             remainder = target - num
#             if self.combinationSum(candidates, remainder):
#                 self.memo[target] = True
#                 return self.memo[target]
#         self.memo[target] = False
#         return self.memo[target]  # 但尝试了所有解法不成功后返回False
#
#
# class Solution:
#     memo = {}
#     res = []
#
#     def combinationSum(self, candidates, target: int):
#         """
#         howSum
#         :param candidates:
#         :param target:
#         :return:
#         """
#         if target in self.memo:
#             return self.memo[target]
#         if target == 0:  # target为0，直接解决
#             return []
#         if target < 0:  # target < 0,无解
#             return None
#
#         for num in candidates:
#             remainder = target - num
#             remainderResult = self.combinationSum(candidates, remainder)  # 迭代成跟小规模的问题
#             if remainderResult is not None:  # 如果子节点返回的不是None（说明有解）
#                 self.res.append(num)  # 在结果中加入num（作为branch）
#                 self.memo[target] = self.res
#                 return self.memo[target]  # 将加入num后的数组返回上一层
#         self.memo[target] = None  # 在遍历完成后都没有结果，说明无解
#         return self.memo[target]
#
#
# class Solution:
#     memo = {}
#     res = []
#
#     def combinationSum(self, candidates, target: int):
#         """
#         howSum
#         :param candidates:
#         :param target:
#         :return:
#         """
#         if target in self.memo:
#             return self.memo[target]
#         if target == 0:
#             return []
#         if target < 0:
#             return None
#
#         shortestResult = None
#
#         for num in candidates:
#             remainder = target - num
#             remainderResult = self.combinationSum(candidates, remainder)
#             self.memo[target] = remainderResult  # 在第一次计算后存入memo
#             if remainderResult is not None:
#                 remainderResult.append(num)  # append方法直接修改数组，没有返回值
#                 combination = remainderResult
#                 self.memo[target] = combination
#                 if shortestResult is None or (len(combination) < len(shortestResult)):
#                     shortestResult = combination
#
#         return shortestResult


class Solution:
    memo = {}
    res = []

    def combinationSum(self, candidates, target: int):
        """
        allSum
        :param candidates:
        :param target:
        :return: 二维数组：第一维：所有解的列表；第二维：每个解的数字组合
        """
        if target in self.memo:
            return self.memo[target]
        if target == 0:  # basecase
            return [[]]
        if target < 0:
            return None
        result = None  # 存储当前一层的所有非0的结果

        for num in candidates:
            remainder = target - num
            remainderResult = self.combinationSum(candidates, remainder)  # 较小尺寸的问题求解，remainderResult为
            self.memo[target] = remainderResult
            if remainderResult is not None:
                for targetResult in remainderResult:  # 将targetResult中的数组展开
                    targetResult.append(num)  # 将本层的操作添加到每一个targetResult中
                    if result is None:  # 将这种非None组合加入这一层的result
                        result = []
                    result.append(targetResult)  # 将所有处理完的solution存入一个数组，返回给上一层
        return result

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        DFS
        :param candidates:
        :param target:
        :return:
        """

        def dfs(candidates, start_idx, target, current_stat, ans):
            if target == 0:
                ans.append(current_stat)
            if target < 0:
                return

            for i in range(start_idx, len(candidates)):
                current_stat.append(candidates[i])
                dfs(candidates, i, target - candidates[i], current_stat[:], ans)
                current_stat.pop()

        ans = []
        dfs(candidates, 0, target, [], ans)
        return ans

test = Solution()
ret = test.combinationSum([2, 3], 7)
print(ret)
test.memo = {}  # 每一个testcase之间清空memo
ret = test.combinationSum([5, 3, 4, 7], 7)
print(ret)
test.memo = {}
ret = test.combinationSum([2, 4], 7)
print(ret)
test.memo = {}
ret = test.combinationSum([2, 3, 5], 8)
print(ret)
test.memo = {}
ret = test.combinationSum([7, 14], 300)
print(ret)
test.memo = {}
