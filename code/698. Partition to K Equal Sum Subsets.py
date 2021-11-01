#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :698. Partition to K Equal Sum Subsets.py
# @Time      :11/1/21 10:08 AM
# @Author    :Eason Tang
from typing import List


# https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/solution/hua-fen-wei-kge-xiang-deng-de-zi-ji-hui-80jmj/

# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         if k == 1:
#             return True
#         target, resid = sum(nums) // k, sum(nums) % k
#         if resid != 0:
#             return False
#
#         def dfs(groups):
#             if not nums:
#                 return True
#             # [前进尝试] 选择数字 看放在哪个篮子里面 for i in range(k)
#             v = nums.pop()
#             print('尝试放置数字{}, 剩余数组={}'.format(v, nums))
#             for i in range(k):
#                 if groups[i] + v <= target:
#                     # [前进尝试]
#                     groups[i] += v
#                     print('尝试放数字{}在位置{}, groups变成={} 向下递归'.format(v, i, groups))
#                     if dfs(groups):
#                         return True
#                     # [后退重置] gorups[i]返回状态
#                     print('数字{}放位置{}尝试失败, groups退回成{}'.format(v, i, groups))
#                     groups[i] -= v
#                 if groups[i] == 0: break  # 细节：减少重复搜索 保证0(没有数的篮子)始终在末尾
#             # [后退重置] 循环所有的group之后 nums再返回之前状态
#             nums.append(v)
#             print('数字{}尝试失败 放回nums nums退回成{} \n---'.format(v, nums))
#             return False
#
#         nums.sort()
#         # 如果最大值大于target则一定不能分成
#         if nums[-1] > target:
#             return False
#         # 如果有等于target的单个数字 则将其先进行处理
#         while nums and nums[-1] == target:
#             nums.pop()
#             k -= 1
#         # 如果k=0 或者 剩下的nums里的值全是0 都return true
#         if k == 0 or not any(nums):
#             return True
#         return dfs([0] * k)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def dfs(nums, k, target, current_group):
            if not nums:  # 如果nums已经被分完了，则已经分好组
                return True

            num = nums.pop()  # 取出下一个要放的数字
            # print('尝试放置数字{}, 剩余数组={}'.format(num, nums))
            for i in range(k):  # 遍历所有的组
                if current_group[i] + num <= target:  # 如果组内原有数字和+欲放入的数字小于target，则可以继续递归
                    current_group[i] += num
                    # print('尝试放数字{}在位置{}, groups变成={} 向下递归'.format(num, i, current_group))
                    if dfs(nums, k, target, current_group):  # 递归进入下一层
                        return True
                    # print('数字{}放位置{}尝试失败, groups退回成{}'.format(num, i, current_group))
                    current_group[i] -= num
                if current_group[i] == 0:  # 如果当前组为空，则跳过，为了保证空的数组在后面，提高效率
                    # 如果有两组均为空，那么搜索第一组的动作其实是与第二组等价的
                    break
            nums.append(num)
            # print('数字{}尝试失败 放回nums nums退回成{} \n---'.format(num, nums))
            return False

        """
        处理一些特殊情况
        """
        target = sum(nums) // k  # 每一组的目标数字，例如数组和为15，平分3组后那每一组的和就为5
        resid = sum(nums) % k
        nums.sort()
        if k == 1:  # 如果只需要分一组，那么一定可以成功分到
            return True
        if resid:  # 如果数组的和不能整除，那么一定无法分组（考虑到给出的nums中只包含整数
            return False
        if nums[-1] > target:  # 如果nums的最大值大大于target也无法分组
            return False
        while nums and nums[-1] == target:  # 如果nums的最大值刚好等于target，那么他们自成一组
            nums.pop()
            k -= 1
        if k == 0 or not any(nums):  # 如果k == 0或所有nums的数字都为0，那么一定可以平分
            return True
        return dfs(nums, k, sum(nums) // k, [0] * k)
