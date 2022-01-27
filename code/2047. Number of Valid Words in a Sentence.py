#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :2047. Number of Valid Words in a Sentence.py
# @Time      :1/26/22
# @Author    :Eason Tang


class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence_arr = sentence.split(" ")

        def is_valid_words(word):
            """
            This function judges if a word is valid
            """
            if not word:
                return False
            has_hypen = False
            for i, ch in enumerate(word):
                if ch.isdigit():
                    # If any digit presented, not valid
                    return False
                if ch == "-":
                    # If we get "-" check if we have 2 hypen, or the hypen is at the begining of the word,
                    # or the hypen is at the end of the word, or is lowe case presented before the hypen, or is lower
                    # case presented after the hypen Don't forget to update the hypen
                    if has_hypen or i == 0 or i == len(word) - 1 or not word[i - 1].islower() or not word[
                        i + 1].islower():
                        return False
                    has_hypen = True
                if ch in '!.,' and i != len(word) - 1:
                    # If the punchuation is presented but not at the end of the word
                    return False

            return True

        return sum(is_valid_words(x) for x in sentence_arr)
