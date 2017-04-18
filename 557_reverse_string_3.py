#! coding=utf8
# Filename    : 557_reverse_string_3.py
# Description : Given a string, you need to reverse the order of characters in each word
#               within a sentence while still preserving whitespace and initial word order.
#               给一个字符串，将字符串中的每个单词反序，保留空格和单词间的顺序。
# Url         : leetcode.com/problems/reverse-words-in-a-string-iii
# Author      : iwannarock
# History:
# 1. 2017/4/19 1:56 , iwannarock, first create


def reverse_words(s):
    """
    :type s: str
    :rtype: str
    """
    word_list = s.split(' ')
    word_reverse_list = [word[::-1] for word in word_list]
    return ' '.join(word_reverse_list)
