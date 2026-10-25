class Solution:
    def closedIsland(self, grid):
        m, n = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 0

            if grid[r][c] == 1:
                return 1

            grid[r][c] = 1

            a = dfs(r - 1, c)
            b = dfs(r + 1, c)
            c1 = dfs(r, c - 1)
            d = dfs(r, c + 1)

            return a and b and c1 and d

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i, j):
                        count += 1

        return count