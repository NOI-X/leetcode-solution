#!/usr/bin/env python
# coding=utf-8

import collections
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n, dp = len(A), [0]
        for v in A: dp.append(dp[-1] + v)

        queue, res = collections.deque(), n + 1
        for i in range(n+1):
            while queue and dp[i] <= dp[queue[-1]]:   # 维护单调递增
                queue.pop()

            while queue and dp[i] - dp[queue[0]] >= K:
                res = min(res, i - queue.popleft())  # 从左边出队，并更新最短距离。

            queue.append(i)

        return res if res < n + 1 else -1
