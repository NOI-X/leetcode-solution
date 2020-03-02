#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        vis = {(0, 0)}
        heapq.heapify(q)
        ans = 0
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < n and (i+1, j) not in vis:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
                vis.add((i+1, j))
            if j + 1 < m and (i, j+1) not in vis:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
                vis.add((i, j+1))
        return ans

