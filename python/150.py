#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        if len(tokens) == 0:
            return 0
        stack = []
        for i in tokens:
            if i == '+':
                b = stack.pop(); a = stack.pop()
                stack.append(a + b)
            elif i == '-':
                b = stack.pop(); a = stack.pop()
                stack.append(a - b)
            elif i == '*':
                b = stack.pop(); a = stack.pop()
                stack.append(a * b)
            elif i == '/':
                b = stack.pop(); a = stack.pop()
                if a * b < 0:
                    stack.append((-1 * a // b) * -1)
                else:
                    stack.append(a // b)
            else:
                stack.append(int(i))
            # print(stack)
        return stack.pop()
