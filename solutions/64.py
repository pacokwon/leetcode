class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue

                if i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[rows - 1][cols - 1]

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    grid = [[1,2,3],[4,5,6]]
    grid = [[1,2],[1,1]]
    print(sol.minPathSum(grid))
