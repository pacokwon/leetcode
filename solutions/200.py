# Number Of Islands

class Solution:
    def numIslands(self, grid):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        rows = len(grid)
        cols = len(grid[0])

        def dfs(x, y):
            grid[x][y] = '0'

            for _dx, _dy in zip(dx, dy):
                newX = x + _dx
                newY = y + _dy

                if not (0 <= newX < rows and 0 <= newY < cols):
                    continue

                if grid[newX][newY] == '0':
                    continue

                dfs(newX, newY)

        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans


if __name__ == "__main__":
    sol = Solution()
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    print(sol.numIslands(grid))
