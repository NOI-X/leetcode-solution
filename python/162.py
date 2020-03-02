#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, -sys.maxint)
        nums.append(-sys.maxint)
        L, R = 0, len(nums) - 1
        while L + 1 < R:
            mid = (L + R) // 2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid - 1
            elif nums[mid] < nums[mid-1]:
                R = mid
            else:
                L = mid

