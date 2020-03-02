#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums, L, R):

        if L >= R:
            return

        pivot = nums[L]
        start, end = L, R
        while start <= end:
            while start <= end and nums[start] < pivot:
                start += 1
            while start <= end and nums[end] > pivot:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        self.quick_sort(nums, L, end)
        self.quick_sort(nums, start, R)

