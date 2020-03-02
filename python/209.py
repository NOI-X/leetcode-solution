#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = 0
        ans = n + 1
        j = 0
        for i in range(n):
            while j < n and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s and j - i < ans:
                ans = j - i
            sum -= nums[i]

        if ans == n + 1:
            return 0
        return ans
