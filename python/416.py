#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)
        if total % 2 == 1:
            return False
        n = len(nums)
        total = total // 2
        dp = [False] * (total + 1)
        dp[0] = True
        for x in nums:
            for j in range(total, x - 1, -1):
                dp[j] = dp[j - x] or dp[j]

        return dp[total]

