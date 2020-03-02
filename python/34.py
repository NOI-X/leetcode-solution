#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        res = []
        L, R = 0, len(nums) - 1
        while L + 1 < R:
            mid = (L + R) / 2
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] == target:
                R = mid
            else:
                L = mid + 1
        if nums[L] == target:
            res.append(L)
        elif nums[R] == target:
            res.append(R)
        else:
            res.append(-1)


        L, R = 0, len(nums) - 1
        while L + 1 < R:
            mid = (L + R) / 2
            if nums[mid] > target:
                R = mid - 1
            elif nums[mid] == target:
                L = mid
            else:
                L = mid + 1
        if nums[R] == target:
            res.append(R)
        elif nums[L] == target:
            res.append(L)
        else:
            res.append(-1)

        return res
