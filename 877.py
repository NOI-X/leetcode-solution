#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[-1] * n for i in range(n)]
        presum = [0] * (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + piles[i]
        self.DFS(piles, 0, n - 1, dp, presum)

        if dp[0][n-1] > presum[n] // 2:
            return True
        return False

    def DFS(self, nums, L, R, dp, presum):
        if dp[L][R] != -1:
            return dp[L][R]
        if L == R:
            dp[L][R] = nums[L]
            return dp[L][R]

        left = presum[R+1] - presum[L+1] - self.DFS(nums, L+1, R, dp, presum) + nums[L]
        right = presum[R] - presum[L] - self.DFS(nums, L, R - 1, dp, presum) + nums[R]

        dp[L][R] = max(left, right)

        return dp[L][R]
