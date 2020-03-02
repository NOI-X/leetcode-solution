#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        L, R = 0, nums[-1] - nums[0]
        while L + 1 < R:
            mid = (L + R) // 2
            cnt = self.check(nums, mid)
            if cnt >= k:
                R  = mid
            elif cnt < k:
                L = mid + 1


        if self.check(nums, L) >= k:
            return L
        else:
            return R

    def check(self, nums, x):
        cnt, j = 0, 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= x:
                j += 1
            cnt += j - i - 1
        return cnt


