#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB = []
        for i in range(len(A)):
            for j in range(len(B)):
                AB.append(A[i] + B[j])

        CD = {}

        for i in range(len(C)):
            for j in range(len(D)):
                if C[i] + D[j] in CD:
                    CD[C[i] + D[j]] += 1
                else:
                    CD[C[i] + D[j]] = 1
        ans = 0
        for i in range(len(AB)):
            if -1 * AB[i] in CD:
                ans += CD[-1 * AB[i]]
        return ans
