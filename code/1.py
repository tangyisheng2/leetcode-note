class Solution:
    # def isValid(self, s: str) -> bool:
    #     # 查看是否为奇数长度
    #     if len(s) % 2 != 0:
    #         return False
    #     stack = ["?"]
    #     pair_dict = {
    #         ")": "(",
    #         "]": "[",
    #         "}": "{",
    #         "?": "?"
    #     }
    #     for ch in s:
    #         if ch in ["(", "[", "{"]:  # 如果是左括号
    #             stack.append(ch)  # push stack
    #         elif ch in pair_dict:  # 如果是右括号
    #             if stack[-1] == pair_dict[ch]:  # 是否与stack top相等
    #                 stack.pop()  # 相等pop stack
    #             else:
    #                 return False  # 相等等匹配失败
    #     if stack == ["?"]:
    #         return True
    #     else:
    #         return False

    def isValid(self, s: str) -> bool:
        while ('()' in s) or ('[]' in s) or ('{}' in s):
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')
        return s == ''



def main():
    print(Solution.isValid(Solution, s="{[]}"))


if __name__ == '__main__':
    main()
