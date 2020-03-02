#!/usr/bin/env python
# coding=utf-8

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.presum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.presum[i+1] = self.presum[i] + nums[i]


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.presum[j + 1] - self.presum[i]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
