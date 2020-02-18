#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        if n == 0:
            return []
        dp = [0]*n
        pre = [-1] * n
        nums.sort()

        dp[0] = 1
        res_index = 0
        for i in range(1, n):
            dp[i] = 1
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j
            if dp[res_index] < dp[i]:
                res_index = i

        return self.getPath(nums, pre, res_index)

    def getPath(self, nums, pre, index):
        if pre[index] == -1:
            return [nums[index]]
        ans = self.getPath(nums, pre, pre[index])
        ans.append(nums[index])
        return ans

