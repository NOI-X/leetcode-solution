#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        cnt = 0
        ans = 0
        j = 0
        for i in range(n):
            while j < n and cnt < K:
                if A[j] == 0:
                    cnt += 1
                j += 1
            while j < n and A[j] == 1:
                j += 1
            ans = max(ans, j - i)
            # print(j)
            if A[i] == 0:
                cnt -= 1

        return ans
