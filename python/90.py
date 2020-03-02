#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0:
            return res
        nums.sort()
        self.DFS(nums, 0, res, [])
        return res

    def DFS(self, nums, start, res, path):

        tmp = path[:]
        res.append(tmp)
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.DFS(nums, i + 1, res, path)
            path.pop(-1)
