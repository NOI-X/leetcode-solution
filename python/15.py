#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        N = len(nums)
        nums.sort()
        res = set()
        for t in range(N - 2):
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if _sum == 0:
                    res.add((nums[t], nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif _sum < 0:
                    i += 1
                else:
                    j -= 1
        return res
