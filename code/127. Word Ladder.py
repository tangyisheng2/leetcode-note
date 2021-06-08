"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

"""
import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List) -> int:
        """
        BFS
        :param beginWord:
        :param endWord:
        :param wordList:
        :return:
        """
        # basecase
        if endWord not in wordList:  # 如果endWord不在wordList中，则无法完成
            return 0

        if beginWord in wordList:  # 将beginWord去除，防止死循环
            wordList.remove(beginWord)

        word_set = set(wordList)  # 不做这一步导致超时？

        # 构建BFS的辅助数据结构queue和visited数组
        queue = collections.deque()
        queue.append(beginWord)

        visited = set(beginWord)

        word_len = len(beginWord)  # 注意题目中各个word长度相同
        step = 1  # 在beginWord存在的情况下，至少需要一步
        while queue:
            cur_queue_size = len(queue)
            for i in range(cur_queue_size):
                cur_word = queue.popleft()
                cur_word_ch_list = list(cur_word)

                # 将单词中的每个字母尝试修改，寻找匹配
                for j in range(word_len):  # 所有的单词长度相同
                    origin_word_ch = cur_word_ch_list[j]  # 保存现有的word，准备后面回复

                    for k in range(26):
                        cur_word_ch_list[j] = chr(ord('a') + k)
                        next_word = ''.join(cur_word_ch_list)  # 构造好的单词

                        if next_word in word_set:
                            if next_word == endWord:  # 如果找到了终点
                                return step + 1
                            if next_word not in visited:  # 如果找到了没有遍历过的元素
                                queue.append(next_word)
                                visited.add(next_word)
                    cur_word_ch_list[j] = origin_word_ch  # 恢复原来的单词（可能未来还需要遍历）
            step += 1
        return 0


test = Solution()
ret = test.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(ret)
