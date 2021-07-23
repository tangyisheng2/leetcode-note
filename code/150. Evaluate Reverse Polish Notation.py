# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   150. Evaluate Reverse Polish Notation.py
@Contact :   tangyisheng2@sina.com
@License :   (C)Copyright 1999-2021, Tang Yisheng
"""
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        data = []
        operator = []

        for elem in tokens:
            if elem in {"+", "-", "*", "/"}:
                if len(data):  # 还是要验证一下data是否为空
                    data1 = data.pop()
                    data2 = data.pop()
                    if elem == "+":
                        data.append(data2 + data1)
                    elif elem == "-":
                        data.append(data2 - data1)
                    elif elem == "*":
                        data.append(data2 * data1)
                    elif elem == "/":  # 正常情况要验证除数是否为0，但是题目已经说过there will not be any division by zero operation，所以不验证
                        data.append(data2 // data1)  # 注意用整除，同时先入栈的作为被除数，后入栈为除数
            else:
                data.append(int(elem))
        return data[0] if data else "ERR"


if __name__ == '__main__':
    test = Solution()
    test.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
