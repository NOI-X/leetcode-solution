#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = 1
        num = 0
        res = 0
        for i in s:
            if i == ' ':
                continue
            if i == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif i == ')':
                res += sign * num
                num = 0
                res *= stack[-1]; stack.pop();
                res += stack[-1]; stack.pop();
            elif i == '+':
                res += sign * num
                num = 0
                sign = 1
            elif i == '-':
                res += sign * num
                num = 0
                sign = -1
            else:
                num = num * 10 + ord(i) - ord('0')
                
        res += sign * num
        return res
