#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        vis = {}
        j = 0
        for i in range(n):
            while j < n and ( s[j] not in vis or vis[s[j]] == 0) :
                vis[s[j]] = 1
                j += 1
            if ans < j - i:
                ans = j - i

            vis[s[i]] -= 1
        return ans


