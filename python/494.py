#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        total = sum(nums)
        if total < S:
            return 0
        total += S
        if total % 2 == 1:
            return 0

        total = total // 2
        dp = [0] * (total + 1)
        dp[0] = 1
        for x in nums:
            for j in range(total, x - 1, -1):
                dp[j] = dp[j - x] + dp[j]

        return dp[total]

