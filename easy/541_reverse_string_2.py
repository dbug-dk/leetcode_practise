#! coding=utf8
# Filename    : 541_reverse_string_2.py
# Description : Given a string and an integer k, you need to reverse the first k characters for every 2k
#               characters counting from the start of the string. If there are less than k characters left,
#               reverse all of them. If there are less than 2k but greater than or equal to k characters,
#               then reverse the first k characters
#               and left the other as original.
#               输入一个字符串s和一个整数k，每2k个字母，将前k个字母颠倒顺序。如果字母数小于k个，则把所有的字母顺序颠倒，
#               如果字母数大于k小于2k，则颠倒前k个字母，剩下的保持不变
# Url         : leetcode.com/problems/reverse-string-ii
# Author      : iwannarock
# History:
# 1. 2017/4/19 2:01 , iwannarock, first create


def reverse_str(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    s_index = 0
    sub_count = 1
    reverse_list = []
    s_len = len(s)
    while s_index < s_len:
        end_index = s_index + k
        if end_index >= s_len:
            substr = s[s_index:]
        else:
            substr = s[s_index:s_index+k]
        if sub_count % 2:
            substr = substr[::-1]
        reverse_list.append(substr)
        sub_count += 1
        s_index += k
    return ''.join(reverse_list)
