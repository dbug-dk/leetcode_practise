#! coding=utf8
# Filename    : 566_reshape_the_matrix.py
# Description : You're given a matrix represented by a two-dimensional array, and two positive integers r and
#               c representing the row number and column number of the wanted reshaped matrix, respectively.
#               The reshaped matrix need to be filled with all the elements of the original matrix in the
#               same row-traversing order as they were. If the 'reshape' operation with given parameters is
#               possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
#               给定一个矩阵和两个正整数r和c，将原矩阵转换为一个r*c的新矩阵，如果给定的r和c非法，直接返回原矩阵
# Url         : leetcode.com/problems/reshape-the-matrix
# Author      : iwannarock
# History:
# 1. 2017/5/1 2:32 , iwannarock, first create


class Solution(object):
    def matrix_reshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        allnums = [reduce(lambda x, y: x + y, nums)]
        if r * c != len(allnums[0]):
            return nums
        ret = []
        for i in range(r):
            ret.append(allnums[0][i*c:(i+1)*c])
        return ret
