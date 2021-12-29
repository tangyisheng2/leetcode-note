#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :846. Hand of Straights.py
# @Time      :12/29/21 10:44 AM
# @Author    :Eason Tang
import collections
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        def update_record(num):
            """
            This function updates record
            """
            frequency[num] -= 1
            if frequency[num] == 0:
                frequency.pop(num)

        def check(num):
            """
            This function checks if the sraight starting from num is valid
            """
            if all([frequency[num + x] > 0 for x in range(groupSize)]):
                return True
            return False

        import collections
        frequency = collections.Counter(hand)
        found = 0
        # for record in sorted(frequency.keys()):
        for record in sorted(hand):
            # Make sure starts from the minimus one
            # Do not use for record in sorted(hashmap) to avoid two valid group which is the same (e.g. [1,1,2,2,3,3])
            if not frequency:
                break
            # print(sorted(frequency))
            if check(record):
                found += 1
                for i in range(groupSize):
                    update_record(record + i)

        return not frequency and found == len(hand) / groupSize

    def isNStraightHand2(self, hand: List[int], groupSize: int) -> bool:
        """
        Greedy Algorithm:
        0. If len(hand) mod groupSize != 0, there is no way to group all the card
        1. Sort the hand and use counter to count the frequency of each number in hands
        2. Iterate though the hand to select x:
            If x is the smallest number in hand, x must be the smallest number in one of the groups (otherwise x will not belong to any group and we can not group all the card)
            2.1 After selecting x, the elements of group is ranges from [x, x + groupSize]
            2.2 check the hashmap, if there is one group that is not valid, the all cards can not be arrange, return False
            2.3 Update the group
        """
        if len(hand) % groupSize > 0:
            return False
        hand.sort()
        cnt = collections.Counter(hand)
        for x in hand:
            if cnt[x] == 0:
                continue
            for num in range(x, x + groupSize):
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True
