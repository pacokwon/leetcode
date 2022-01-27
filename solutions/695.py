# Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]

        def dfs(r, c):
            grid[r][c] = 0

            count = 1
            for _dx, _dy in zip(dx, dy):
                newR = r + _dx
                newC = c + _dy

                if not (0 <= newR < rows and 0 <= newC < cols):
                    continue

                if grid[newR][newC] == 0:
                    continue

                count += dfs(newR, newC)

            return count

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))

        return ans
