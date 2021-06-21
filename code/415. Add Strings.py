# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         int_num1, int_num2 = 0, 0
#         stack = []
#         res = ""
#         for i in range(len(num1)):  # 将string转为int
#             int_num1 = int_num1 * 10 + (ord(num1[i]) - ord("0"))
#
#         for i in range(len(num2)):  # 将string转为int
#             int_num2 = int_num2 * 10 + (ord(num2[i]) - ord("0"))
#
#         int_res = int_num1 + int_num2
#
#         while int_res >= 1:  # 求得stack中的每个数字
#             stack.append(int(int_res % 10))
#             int_res = int_res / 10
#
#         while stack:
#             res = f"{res}{chr(stack.pop() + ord('0'))}"
#
#         if res == "":
#             return "0"
#
#         return res
#
#         # return str(int_res)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i = len(num1) - 1  # 创建两个指向末尾的指针
        j = len(num2) - 1
        carry = 0  # 进位

        while i >= 0 or j >= 0 or carry:  # 从后向前移动指针遍历num1和num2
            n1 = int(num1[i]) if i >= 0 else 0  # 获取num1和num2的数字
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry  # 两数字加上进位位相加

            res = str(tmp % 10) + res  # 将相加结果放在原数组的「前面」
            carry = tmp // 10
            # carry = 0   # 相加完时候carry位置0
            # if tmp >= 10:   # 如果加出来>10需要进位
            #     carry = 1
            i -= 1  # 指针前移
            j -= 1

        return res if not carry else "1" + res

        # return str(int_res)


test = Solution()
ret = test.addStrings(num1="17849419788197",
                      num2="877968504004372811")
print(ret)
