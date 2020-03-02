#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        dp1 = [0] * n

        dp1[0] = nums[0]
        for i in range(1, n - 1):
            if i == 1:
                dp1[i] = max(dp1[i-1], nums[i])
            else:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        dp1[n-1] = dp1[n - 2]
        dp2 = [0] * n
        dp2[0] = 0
        for i in range(1, n):
            if i == 1:
                dp2[i] = max(dp2[i-1], nums[i])
            else:
                dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        return max(dp1[n-1], dp2[n-1])
