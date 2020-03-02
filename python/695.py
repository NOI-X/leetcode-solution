#!/usr/bin/env python
# coding=utf-8

from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        vis = [[0]*len(grid[0]) for i in range(len(grid))]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    ans = max(ans, self.BFS(grid, vis, i, j))

        return ans

    def BFS(self, g, vis, x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        Q = deque()
        Q.append((x, y))
        vis[x][y] = 1
        cnt = 1
        while len(Q) > 0:
            curx, cury = Q.popleft()
            for i in range(4):
                x = curx + dx[i]
                y = cury + dy[i]
                if x < 0 or y < 0 or x >= len(g) or y >= len(g[0]) or g[x][y] == 0 or vis[x][y] == 1:
                    continue
                cnt += 1
                vis[x][y] = 1
                Q.append((x, y))

        return cnt
