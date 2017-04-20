#! coding=utf8
# Filename    : 241_different_ways_to_add_parentheses.py
# Description : Given a string of numbers and operators, return all possible results from computing all the
#               different possible ways to group numbers and operators. The valid operators are +, - and *.
#               输入一个算术表达式字符串（只包含数字和+，-，*），通过在两个数字之间加括号，返回所有可能的计算结果，
# Url         : leetcode.com/problems/different-ways-to-add-parentheses
# Author      : iwannarock
# History:
# 1. 2017/4/19 3:04 , iwannarock, first create


class Solution(object):
    def diff_ways_to_compute(self, input_str):
        """
        :type input_str: str
        :rtype: List[int]
        """
        ret = []
        symbols = ['*', '-', '+']
        found_symbol = False
        for index, character in enumerate(input_str):
            if character in symbols:
                if index == 0 or input_str[index-1] in symbols:
                    continue
                found_symbol = True
                left_results = self.diff_ways_to_compute(input_str[:index])
                right_results = self.diff_ways_to_compute(input_str[index+1:])
                for lnum in left_results:
                    for rnum in right_results:
                        ret.append(eval('%d%s%d' % (lnum, character, rnum)))
        if not found_symbol:
            ret.append(int(input_str))
        return ret
