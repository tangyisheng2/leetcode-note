#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :4. Median of Two Sorted Arrays.py
# @Time      :4/29/22
# @Author    :Eason Tang
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            """
            Basecase:
            已知两数组合并后的长度，求他的中位数相当于求两数组合并后第 k = (m + n) // 2 小的数（长度为奇数情况）
            或 k = (m + n) // 2 和 k = ((m + n) // 2 + 1 ) 的平均值 （长度为基数的情况）
            1. 寻找数组中的第一个数（？）：nums1 = [1,3], nums2 = [2] -> k = 1 -> return min(nums1[0], nums2[0])
            2. 其中一个数组为空（所有数字都已经找完了且均小于第k个数）：
                nums1 = [], nums2 = [1,2,3] -> return nums2[index2 + k - 1] (返回另外一个数组的第k个数)

            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """

            index1, index2 = 0, 0  # nums1 和 nums2 的偏移量
            while True:
                # 特殊情况
                if index1 == m:  # 数组1已经到达末尾
                    return nums2[index2 + k - 1]  # 返回数组2的第 (index2 + k - 1) 个数字
                if index2 == n:  # 数组2已经到达末尾
                    return nums1[index1 + k - 1]  # 返回数组2的第 (index2 + k - 1) 个数字
                if k == 1:  # 如果要寻找的中位数下标为1
                    return min(nums1[index1], nums2[index2])  # 返回 nums1 和 nums2 中的最小值

                # 正常情况
                newIndex1 = min(index1 + k // 2 - 1, m - 1)  # 新的偏移量为旧的偏移量 + 本轮排除的数字个数
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]  # 新的中位数判定下标
                if pivot1 <= pivot2:  # 如果nums1的判定下标处数字 < nums2的判定下标处数字
                    k -= newIndex1 - index1 + 1  # 更新k值： 减去nums排除的素质个数
                    index1 = newIndex1 + 1  # 更新index1的下标
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:  # 如果合并后的数组是基数，则选择 第(k + 1 // 2)个 数字
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(
                totalLength // 2 + 1)) / 2  # 如果合并后的数组是偶数，则选择 第 (k // 2) 和 (k // 2 + 1) 的平均值
