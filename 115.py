#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n = len(t)
        m = len(s)

        dp = [[0] * (m+1) for i in range(n+1)]

        for i in range(m + 1):
            dp[0][i] = 1

        for i in range(n):
            for j in range(m):
                if t[i] == s[j]:
                    dp[i+1][j+1] = dp[i+1][j] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]

        return dp[n][m]
