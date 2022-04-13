from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        dx, dy = 1, 1
        x, y = 0, -1
        count = 1

        while True:
            for _ in range(n):
                y += dy
                mat[x][y] = count
                count += 1

            dy = -dy
            n -= 1
            if n == 0:
                break

            for _ in range(n):
                x += dx
                mat[x][y] = count
                count += 1
            dx = -dx

        return mat

if __name__ == "__main__":
    n = 4
    print(Solution().generateMatrix(n))

