#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        if n <= 2:
            return 0
        dp = [[-1] * n for i in range(n)]

        self.DFS(nums, 0, n - 1, dp)
        return dp[0][n-1]

    def DFS(self, nums, L, R, dp):
        if L + 1 == R:
            return 0
        if dp[L][R] != -1:
            return dp[L][R]
        ans = 0
        for i in range(L+1, R):
            ans = max(ans, nums[L]*nums[i]*nums[R] + self.DFS(nums, L, i, dp) + self.DFS(nums, i, R, dp))

        dp[L][R] = ans
        return dp[L][R]
