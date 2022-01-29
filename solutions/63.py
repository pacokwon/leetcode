# Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        if obstacleGrid[0][0] == 1:
            return 0

        # base case
        dp[1][1] = 1

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if i == 1 and j == 1:
                    continue

                if obstacleGrid[i - 1][j - 1] == 1:
                    continue

                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows][cols]

if __name__ == "__main__":
    sol = Solution()
    # obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    obstacleGrid = [[0,1],[0,0]]
    print(sol.uniquePathsWithObstacles(obstacleGrid))
