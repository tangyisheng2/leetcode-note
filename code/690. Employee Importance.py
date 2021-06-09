"""
You have a data structure of employee information, which includes the employee's unique id, their importance value, and their direct subordinates' id.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the subordinates of the ith employee.
Given an integer id that represents the ID of an employee, return the total importance value of this employee and all their subordinates.

Example 1:
Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
They both have importance value 3.
So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Example 2:
Input: employees = [[1,2,[5]],[5,-3,[]]], id = 5
Output: -3


Constraints:
1 <= employees.length <= 2000
1 <= employees[i].id <= 2000
All employees[i].id are unique.
-100 <= employees[i].importance <= 100
One employee has at most one direct leader and may have several subordinates.
id is guaranteed to be a valid employee id.

"""
import collections

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# class Solution:  # DFS
#     def getImportance(self, employees: List['Employee'], idx: int) -> int:
#         hash_map = {employee.id: employee for employee in employees}  # 创建哈希表
#
#         def dfs(idx: int) -> int:
#             employee = hash_map[idx]
#             total = employee.importance + sum(dfs(subIdx) for subIdx in employee.subordinates)  # 递归
#             return total
#
#         return dfs(idx)

class Solution:  # BFS
    def getImportance(self, employees: List['Employee'], idx: int) -> int:
        hash_map = {employee.id: employee for employee in employees}

        queue = collections.deque()
        queue.append(idx) # deque中元素要iterable
        # 两种写法：
        # queue = collections.deque([idx]) # 要死直接生成deque必须传入iterable
        # or
        # queue = collections.deque()
        # queue.append(idx) # append可以直接append int
        sum_importance = 0
        while queue:
            employee_idx = queue.popleft()
            employee = hash_map[employee_idx]
            sum_importance += employee.importance
            queue.append(sub_employee for sub_employee in employee.subordinates)

        return sum_importance


test = Solution()
ret = test.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)
print(ret)