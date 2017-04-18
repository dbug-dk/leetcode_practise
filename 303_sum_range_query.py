#! coding=utf8
# Filename    : 303_sum_range_query.py
# Description : Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#               1.You may assume that the array does not change.
#               2.There are many calls to sumRange function.
#               给一个整形数组，求数组下标i到下标j（包括）之间的数之和。
#               两个前提：
#               1.整形数组给定后不会变化
#               2.会多次获取数组区间的和（保证查询效率）
# Url         : leetcode.com/problems/range-sum-query-immutable
# Author      : iwannarock
# History:
# 1. 2017/4/19 2:11 , iwannarock, first create


class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        sums = 0
        self.sumList = []
        for num in nums:
            sums += num
            self.sumList.append(sums)

    def sum_range(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sumList[j]
        return self.sumList[j] - self.sumList[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sum_range(i, j)
