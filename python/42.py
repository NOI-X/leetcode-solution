#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        pre = [0] * (n + 2)
        suf = [0] * (n + 2)
        ans = 0
        for i in range(n):
            pre[i+1] = max(pre[i], height[i])
        for i in range(n - 1, -1, -1):
            suf[i + 1] = max(suf[i + 2], height[i])
            ans += min(pre[i+1], suf[i + 1]) - height[i]
        return ans
