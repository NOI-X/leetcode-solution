#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        n = len(coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for x in coins:
            for j in range(x, amount + 1):
                dp[j] = min(dp[j], dp[j - x] + 1)

        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]

