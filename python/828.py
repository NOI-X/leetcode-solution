#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        res, mod, f = 0, 10**9 + 7, 0
        m, n = [0]*26, [0]*26
        for i, v in enumerate(S):
            t = ord(v) - 65
            f = f + 1 + i - 2 * m[t] + n[t]
            res = (res + f) % mod
            n[t], m[t] = m[t], i + 1
        return res

