# Shortest Path in Binary Matrix

from queue import Queue

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dx = [1, 1, 1, 0, -1, -1, -1, 0]
        dy = [1, 0, -1, -1, -1, 0, 1, 1]

        if grid[0][0] == 1:
            return -1

        if rows == 1 and cols == 1:
            return 1

        visited = [[False] * cols for _ in range(rows)]

        q = Queue()
        # path from top-left to (0, 0) is length 1
        q.put((0, 0, 1))
        visited[0][0] = True

        while not q.empty():
            r, c, length = q.get()

            for _dx, _dy in zip(dx, dy):
                newR = r + _dx
                newC = c + _dy

                if not (0 <= newR < rows and 0 <= newC < cols):
                    continue

                if grid[newR][newC] == 1:
                    continue

                if visited[newR][newC]:
                    continue

                if newR == rows - 1 and newC == cols - 1:
                    return length + 1

                visited[newR][newC] = True
                q.put((newR, newC, length + 1))

        return -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[1,0,0],[1,1,0],[1,1,0]]
    grid = [[0, 1], [1, 0]]
    grid = [[0]]
    print(sol.shortestPathBinaryMatrix(grid))
