#! coding=utf8
# Filename    : 461_hamming_distance.py
# Description : The Hamming distance between two integers is the number of positions at which the
#               corresponding bits are different. Given two integers x and y, calculate the Hamming
#               distance.
#               给定两个整数x和y，计算汉明距离（两个数字的二进制中，对应位不同的个数）
# Url         : leetcode.com/problems/hamming-distance
# Author      : iwannarock
# History:
# 1. 2017/5/1 2:10 , iwannarock, first create


class Solution(object):
    def hamming_distance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        count = 0
        while xor:
            if xor % 2 == 1:
                count += 1
            xor /= 2
        return count
