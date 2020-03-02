#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        p = []
        for i in range(len(nums)):
            p.append((nums[i], i))
        p.sort()
        i, j = 0, len(nums)-1
        while i < j:
            if p[i][0] + p[j][0] > target:
                j -= 1
            elif p[i][0] + p[j][0] < target:
                i += 1
            else:
                L = min(p[i][1], p[j][1])
                R = max(p[i][1], p[j][1])
                return [L, R]
