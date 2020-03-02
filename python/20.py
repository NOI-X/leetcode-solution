#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = "([{"
        right = ")]}"

        stack = []
        for i in s:
            if left.find(i) != -1:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                index = right.find(i)
                if left.find(stack[-1]) == index:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
