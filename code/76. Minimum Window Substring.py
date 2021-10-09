#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :76. Minimum Window Substring.py
# @Time      :10/8/21 4:57 PM
# @Author    :Eason Tang
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        need = collections.defaultdict(int)  # 记录了所有数组中需要包含的字母以及个数
        for c in t:  # 计算t中所需要包含的字母个数
            need[c] += 1
        needCnt = len(t)  # 计算所需要包含字母的数量 -> ABCA = 4
        i = 0  # 左指针
        res = (0, float('inf'))  # tuple包含了左右指针下标
        for j, c in enumerate(s):  # j右指针
            if need[c] > 0:  # 说明需要更多的char
                needCnt -= 1  # 需要字母总计数 -1
            need[c] -= 1  # 更新表
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i（左指针），排除多余元素
                    c = s[i]
                    if need[c] == 0:  # 当need[c]已经是0的时候，在增加左边界就不符合要求了
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果，更新最小值
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


# 作者：Mcdull0921
# 链接：https://leetcode-cn.com/problems/minimum-window-substring/solution/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/

test = Solution()
test.minWindow(s="ADOBECODEBANC", t="ABC")
