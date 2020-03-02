
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        res = 0
        vis = [ [0] * m for i in range(n)]
        empty = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    empty += 1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = self.DFS(grid, i, j, vis, empty)
        return res

    def DFS(self, grid, x, y, vis, empty):
        # print(x, y, empty)
        n, m = len(grid), len(grid[0])

        if grid[x][y] == 2 and empty == 1:
            return 1
        if grid[x][y] == 2:
            return 0

        vis[x][y] = 1
        res = 0
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if not self.check(nx, ny, n, m, vis, grid):
                continue

            nnx, nny = nx + d[i][0], ny + d[i][1]
            side = 0
            if i < 2:
                side = 2

            sx_1, sy_1 = nx + d[side][0], ny + d[side][1]
            sx_2, sy_2 = nx + d[side^1][0], ny + d[side^1][1]

            if self.checkCircle(nnx, nny, n, m, vis, grid) and self.check(sx_1, sy_1, n, m, vis, grid) and self.check(sx_2, sy_2, n, m, vis, grid):
                continue

            res += self.DFS(grid, nx, ny, vis, empty - 1)

        vis[x][y] = 0
        return res

    def checkCircle(self, x, y, n, m, vis, grid):
        return x >= 0 and y >=0 and x < n and y < m and (vis[x][y] == 1)

    def check(self, x, y, n, m, vis, grid):
        return x >= 0 and y >= 0 and x < n and y < m and vis[x][y] == 0 and grid[x][y] != -1
