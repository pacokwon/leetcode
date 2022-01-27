# Rotting Oranges

from queue import Queue

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        q = Queue()
        # 0: empty, 1: fresh, 2: rotten
        freshCount = 0
        for r in range(rows):
            for c in range(cols):
                o = grid[r][c]

                if o == 1:
                    freshCount += 1
                elif o == 2:
                    # this cell is rotten at day 0
                    q.put((r, c, 0))

        if freshCount == 0:
            return 0

        count = 0
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        while not q.empty():
            # r, c was rotten on `days`
            r, c, days = q.get()

            newDays = days + 1
            for _dx, _dy in zip(dx, dy):
                newR = r + _dx
                newC = c + _dy

                if not (0 <= newR < rows and 0 <= newC < cols):
                    continue

                if grid[newR][newC] != 1:
                    continue

                grid[newR][newC] = 2
                count += 1
                if count == freshCount:
                    return newDays

                q.put((newR, newC, newDays))

        return -1

if __name__ == "__main__":
    sol = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    grid = [[0, 2]]
    print(sol.orangesRotting(grid))
