#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        presum = {0: 1}
        ans, sum = 0, 0
        for a in A:
            sum += a
            if sum % K in presum:
                ans += presum[sum % K]
                presum[sum % K] += 1
            else:
                presum[sum % K] = 1

        return ans
