#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        return self.findKth(nums, 0, len(nums) - 1, len(nums) - k + 1)


    def findKth(self, nums, L, R, k):

        if L == R and k == 1:
            return nums[L]
        # print(L, R, k)
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

        if end - L + 1 >= k:
            return self.findKth(nums, L, end, k)
        elif start - L < k:
            return self.findKth(nums, start, R, k - (start - L) )
        else:
            return nums[end + 1]
