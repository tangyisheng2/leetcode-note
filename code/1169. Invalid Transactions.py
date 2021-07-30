# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1169. Invalid Transactions.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        transactions_by_person = {}  # 按交易对象分类
        invalid = [False] * n  # 记录非法的id
        ans = []
        count = 0
        for record in transactions:
            name, time, amount, city = record.split(",")  # 从记录中提取相关信息
            time, amount = int(time), int(amount)  # 转换成int方便下面比较

            if name not in transactions_by_person:  # 增加一个记录，防止下面查找时的index error
                transactions_by_person[name] = set()

            for pre_record in transactions_by_person[name]:  # 查找先前记录
                if pre_record[3] != city and abs(pre_record[1] - time) <= 60:
                    invalid[count] = True  # 注意非法是两条记录一起非法的
                    invalid[pre_record[0]] = True

            if amount > 1000:  # 检查当前记录是否非法
                invalid[count] = True

            transactions_by_person[name].add((count, time, amount, city))  # 添加到记录中
            count += 1  # 记录+1

        for i in range(n):
            if invalid[i]:
                ans.append(transactions[i])

        return ans

