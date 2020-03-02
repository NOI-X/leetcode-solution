#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(n):
            dp[i+1] = 0
            if s[i] != '0':
                dp[i+1] += dp[i]
            if self.check(i, s):
                dp[i+1] += dp[i-1]
            # print(dp[i])

        return dp[n]

    def check(self, i, s):
        if i == 0:
            return False
        if s[i-1] != '1' and s[i-1] != '2':
            return False

        x = (ord(s[i-1]) - ord('0')) * 10 + ord(s[i]) - ord('0')

        if x > 0 and x <= 26:
            return True
        return False

