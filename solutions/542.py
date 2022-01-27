# 01 Matrix

from queue import Queue

class Solution:
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        res = [[-1] * cols for _ in range(rows)]

        q = Queue()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.put((r, c, 0))
                    res[r][c] = 0

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        while not q.empty():
            r, c, dist = q.get()
            newDist = dist + 1
            for _dx, _dy in zip(dx, dy):
                newR = r + _dx
                newC = c + _dy

                if not (0 <= newR < rows and 0 <= newC < cols):
                    continue

                if res[newR][newC] == -1 or newDist < res[newR][newC]:
                    res[newR][newC] = newDist
                    q.put((newR, newC, newDist))

        return res

if __name__ == "__main__":
    sol = Solution()
    mat = [[0,0,0],[0,1,0],[0,0,0]]
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(sol.updateMatrix(mat))
