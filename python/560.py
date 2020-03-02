#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        presum = {0: 1}
        sum, ans = 0, 0
        for num in nums:
            sum += num
            if sum - k in presum:
                ans += presum[sum - k]
            if sum in presum:
                presum[sum] += 1
            else:
                presum[sum] = 1

        return ans
