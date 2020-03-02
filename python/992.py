#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        ans = 0
        vis1, vis2 = {}, {}
        j1, j2 = 0, 0
        cnt1, cnt2 = 0, 0
        for i in range(n):
            while j1 < n and cnt1 < K:
                if A[j1] not in vis1 or vis1[A[j1]] == 0:
                    cnt1 += 1
                    vis1[A[j1]] = 1
                else:
                    vis1[A[j1]] += 1
                j1 += 1
            while j2 < n and cnt2 <= K:
                if A[j2] not in vis2 or vis2[A[j2]] == 0:
                    cnt2 += 1
                    vis2[A[j2]] = 1
                else:
                    vis2[A[j2]] += 1
                j2 += 1
           # print(j1, j2)
            if cnt1 >= K:
                ans += j2 - j1
            if cnt2 == K:
                ans += 1
            vis1[A[i]] -= 1
            vis2[A[i]] -= 1
            if vis1[A[i]] == 0:
                cnt1 -= 1
            if vis2[A[i]] == 0:
                cnt2 -= 1
        return ans
