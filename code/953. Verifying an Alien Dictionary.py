from typing import List


# class Solution:
#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         """
#         题目要求：
#         给定一系列待验证的单词，通过外星人的首字母顺序表来验证这些单词的排序是否有序
#         在题目中，我们可以比较两个单词的第一个首字母的不同来判定这两个单词是否符合顺序
#         同时，由于单词的有序性是可以传递的，因此如果a,b有序，b,c有序，则a,c也有序
#         但所有的单词都是有序的时候，返回true
#         :param words: 待验证的单词
#         :param order: 外星人的首字母顺序，我们需要按照这个顺序来验证单词是否有序
#         :return: 排序是否有效
#         """
#
#         for j in range(1, len(words)):  # 第二个单词
#             i = j - 1  # 第一个单词
#
#             word1 = words[i]  # 第一个单词
#             word2 = words[j]
#
#             ch_i, ch_j = 0, 0  # 设定指向两个单词的指针并开始比较
#             while ch_i < word1.__len__() and ch_j < word2.__len__():  # 如果word1短于word2，那么word1和word2还是有序的
#                 if word1[ch_i] == word2[ch_j] and \
#                         ch_i < len(word1) - 1 and ch_j < len(word2) - 1:  # 找到第一个不同的index
#                     ch_i += 1
#                     ch_j += 1
#                 # elif order.index(word1[ch_i]) < order.index(word2[ch_j]):  # 两个单词之间有序
#                 #     break
#                 # elif ch_i == len(word1) - 1 and len(word1[ch_i:]) < len(word2[ch_j:]):
#                 #     break
#                 # else:  # 两个单词之间不是有序，则可以开始比较下一个单词
#                 #     return False
#
#             if order.index(word1[ch_i]) < order.index(word2[ch_j]):  # 两个单词之间有序
#                 break
#             elif ch_i == len(word1) - 1 and len(word1[ch_i:]) < len(word2[ch_j:]):  # word1已经到末尾且word1长度比word2短
#                 break
#
#             return False
#
#         return True
#
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        题目要求：
        给定一系列待验证的单词，通过外星人的首字母顺序表来验证这些单词的排序是否有序
        1. 在题目中，我们可以比较两个单词的第一个首字母的不同来判定这两个单词是否符合顺序
        2. 在单词中各字母都相同的时候，长度较短的单词应该排在长度较长的单词前面
        3. 同时，由于单词的有序性是可以传递的，因此如果a,b有序，b,c有序，则a,c也有序
        当所有的单词都是有序的时候，返回true
        :param words: 待验证的单词
        :param order: 外星人的首字母顺序，我们需要按照这个顺序来验证单词是否有序
        :return: 排序是否有效
        """
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # 找到word1和word2的第一个不同，word1[j] != word2[j]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:  # 找到了第一个不相同的字母
                    if order.index(word1[j]) > order.index(word2[j]):
                        return False  # 在比较到第一个不同的字母就要终止比较
                    break  # 当比较到末尾两字母的仍然没有重复的时候中止比较，跳到下面的else

            # 在单词所有字母相同但是单词长度不同时，长度较短的单词应排在前面
            else:
                if len(word1) > len(word2):
                    return False

        return True


test = Solution()
ret = test.isAlienSorted(words=["hello", "hello"], order="abcdefghijklmnopqrstuvwxyz")
print(ret)
