#! coding=utf8
# Filename    : 476_number_complement.py
# Description : Given a positive integer, output its complement number. The complement strategy is to flip
#               the bits of its binary representation.
#               给定一个正整数，求补数（32位，高位0不翻转），eg: 5(101)-> 2(010)
# Url         : leetcode.com/problems/number-complement
# Author      : iwannarock
# History:
# 1. 2017/5/1 2:50 , iwannarock, first create


class Solution(object):
    def find_complement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = self.get_bit_num(num)
        return ~num & n

    def get_bit_num(self, num):
        n = 0
        count = 0
        while num:
            num /= 2
            n += 2**count
            count += 1
        return n
