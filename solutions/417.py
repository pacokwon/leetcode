# Pacific Atlantic Water Flow
from pprint import pprint

class Solution:
    def dfs(self, heights, r, c, flowable):
        flowable[r][c] = True
        height = heights[r][c]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for _dx, _dy in zip(dx, dy):
            newX = r + _dx
            newY = c + _dy

            if not (0 <= newX < len(flowable) and 0 <= newY < len(flowable[0])):
                continue

            if flowable[newX][newY]:
                continue

            if height <= heights[newX][newY]:
                self.dfs(heights, newX, newY, flowable)

    def pacificAtlantic(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            if not pacific[i][0]:
                self.dfs(heights, i, 0, pacific)

        for i in range(cols):
            if not pacific[0][i]:
                self.dfs(heights, 0, i, pacific)

        for i in range(rows):
            if not atlantic[i][cols - 1]:
                self.dfs(heights, i, cols - 1, atlantic)

        for i in range(cols):
            if not atlantic[rows - 1][i]:
                self.dfs(heights, rows - 1, i, atlantic)

        ans = []
        for r in range(rows):
            for c in range(cols):
                if pacific[r][c] and atlantic[r][c]:
                    ans.append([r, c])

        return ans

if __name__ == "__main__":
    sol = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    # heights = [[2,1],[1,2]]
    print(sol.pacificAtlantic(heights))
