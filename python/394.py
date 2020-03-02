#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = 0
        string = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(string)
                stack.append(num)
                string = ''
                num = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                string = prestring + prenum * string
            elif char.isdigit():
                num = num * 10 + int(char)
            else:
                string += char
        return string
