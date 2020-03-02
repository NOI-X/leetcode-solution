#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.DFS(candidates, 0, target, res, [])
        return res

    def DFS(self, nums, start, target, res, path):
        if target == 0:
            res.append(path[:])
            return
        if len(nums) == start:
            return

        for i in range(start, len(nums)):
            if target - nums[i] < 0:
                continue
            path.append(nums[i])
            self.DFS(nums, i, target - nums[i], res, path)
            path.pop(-1)

