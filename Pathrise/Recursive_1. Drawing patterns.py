#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Recursive_1. Drawing patterns.py
# @Time      :12/22/21 12:01 AM
# @Author    :Eason Tang
def triangle(n: int):
    """
    Should draw:
    n=6
    #
    ##
    ###
    ####
    #####
    ######
    :param n: count
    :return:
    """

    def repeat(character, count):
        """
        This function prints count * character recursively
        :param character: character to print
        :param count:
        :return:
        """
        if count == 1:
            print(character)
        else:
            print(character,
                  end='')  # In Python, print() adds a line break at the end unless we add end=''. We only want to add the line break at the base case.
            repeat(character, count - 1)

    def traingleRec(i: int):
        """
        This function recursively draw n lines of pattern
        :param i:
        :return:
        """
        if i > n:
            return
        repeat('#', i)
        traingleRec(i + 1)

    # repeat('#', 5)
    traingleRec(1)  # Recursion Entry Point: Our recursion starts at 1x "#"


def wedge(n: int):
    """
    Should draw:
    n=6
    #
    ##
    ###
    ####
    #####
    ######
    :param n: count
    :return:
    """

    def repeat(character, count):
        """
        This function prints count * character recursively
        :param character: character to print
        :param count:
        :return:
        """
        if count == 1:
            print(character)
        else:
            print(character,
                  end='')  # In Python, print() adds a line break at the end unless we add end=''. We only want to add the line break at the base case.
            repeat(character, count - 1)

    def traingleRec(i: int):
        """
        This function recursively draw n lines of pattern
        :param i:
        :return:
        """
        if i > n:
            return
        repeat('#', i)
        traingleRec(i + 1)
        repeat('#', i)

    # repeat('#', 5)
    traingleRec(1)  # Recursion Entry Point: Our recursion starts at 1x "#"


def matrix(m, n):
    def repeat(character, count):
        """
        This function prints count * character recursively
        :param character: character to print
        :param count:
        :return:
        """

        if count == 1:
            print(character)
        else:
            print(character,
                  end='')  # In Python, print() adds a line break at the end unless we add end=''. We only want to add the line break at the base case.
            repeat(character, count - 1)

    if m == 1:
        repeat('#', n)
    else:
        repeat('#', n)
        matrix(m - 1, n)


def pattern(n):
    def repeat(ch, k):
        if k == 1:
            print(ch)
        else:
            print(ch, end='')
            repeat(ch, k - 1)

    if n == 1:
        print('x')
    else:
        pattern(n - 1)
        repeat('x', n)
        pattern((n - 1))


def pattern2(n):
    def repeat(ch, k):
        """
        This function prints ch * k
        :param ch:
        :param k:
        :return:
        """
        if k == 1:
            print(ch)
        else:
            print(ch, end='')
            repeat(ch, k - 1)

    def triangle(count, max_count):
        """
        This function prints a small triangle
        :param count:
        :param max_count:
        :return:
        """
        if count > max_count:
            return
        repeat('x', count)
        triangle(count + 1, max_count)

    def repeat_triangle(count, max_count):
        """
        This function prints the big triangle
        :param count:
        :param max_count:
        :return:
        """
        if count > max_count:
            return

        triangle(1, count)
        repeat_triangle(count + 1, max_count)

    repeat_triangle(1, n)  # START RECURSION


def diamond(n):
    """
    Problem: print a diamond of height 2n-1 without using iterative loops.
    Example:
    n = 5:
    ....X....
    ...XXX...
    ..XXXXX..
    .XXXXXXX.
    XXXXXXXXX
    .XXXXXXX.
    ..XXXXX..
    ...XXX...
    ....X....
    :param n:
    :return:
    """

    def repeat(ch, count):
        """
        This function prints the k-th line
        :return:
        """
        if count == 0:
            return
        else:
            print(ch, end='')
            repeat(ch, count - 1)

    def print_k_line(k):
        """
        This function prints the k-th line
        :param k:
        :return:
        """
        nonlocal reach_longest
        if reach_longest and k == n:
            return
        if k == n:
            reach_longest = True
        repeat("#", n - k)
        repeat("X", 2 * (k - 1) + 1)
        repeat("#", n - k)
        print('')

    def repeat_diamond(count):
        """
        This function prints the diamond
        :return:
        """
        if count > n:
            return

        print_k_line(count)
        repeat_diamond(count + 1)
        print_k_line(count)

    reach_longest = False
    repeat_diamond(1)


def star(n):
    """
    **Problem:** print a star of height 2n-1 without using iterative loops.
    Example:
    n = 5:
    \    |    /
     \   |   /
      \  |  /
       \ | /
    ----X----
       / | \
      /  |  \
     /   |   \
    /   |     \
    :param n:
    :return:
    """

    def repeat(ch, count):
        """
        This function print ch * count without creating a new line
        :param ch:
        :param count:
        :return:
        """
        if count <= 0:
            return
        else:
            print(ch, end='')
            repeat(ch, count - 1)

    def print_k_th_line(k, upper_half):
        """
        this function prints k_th line
        :param k:
        :return:
        """
        nonlocal reach_longest
        if k == n and reach_longest:
            return
        if k == n:
            repeat('-', n - 1)
            repeat('X', 1)
            repeat('-', n - 1)
            print('')
            reach_longest = True
            return
        repeat(' ', k - 1)
        repeat('\\' if upper_half else '/', 1)
        repeat(' ', n - 1 - k)
        repeat('|', 1)
        repeat(' ', n - 1 - k)
        # repeat(' ', k - 1)
        repeat('/' if upper_half else '\\', 1)
        print('')

    def repeat_star(count, max_count):
        """
        This function draw start recursively
        :param count:
        :param max_count:
        :return:
        """
        if count > max_count:
            return
        print_k_th_line(count, True)
        repeat_star(count + 1, max_count)
        print_k_th_line(count, False)

    reach_longest = False
    repeat_star(1, n)
    # print_k_th_line(1)

# triangle(10)
# wedge(10)
# matrix(5, 5)

# pattern(3)
# pattern2(4)

diamond(5)
# star(5)
