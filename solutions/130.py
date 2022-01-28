# Surrounded Regions
from pprint import pprint

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c, visited, path):
            border = r == 0 or r == rows - 1 or c == 0 or c == cols - 1
            visited[r][c] = True
            path.append((r, c))

            for _dx, _dy in zip(dx, dy):
                newR = r + _dx
                newC = c + _dy

                if not (0 <= newR < rows and 0 <= newC < cols):
                    continue

                if board[newR][newC] == 'O' and not visited[newR][newC]:
                    # bug was here, because the two operands were initially swapped
                    border = dfs(newR, newC, visited, path) or border

            return border

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == 'X' or visited[r][c]: continue

                path = []
                border = dfs(r, c, visited, path)
                if border: continue
                for rr, cc in path:
                    board[rr][cc] = 'X'


# if __name__ == "__main__":
#     sol = Solution()
#     board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#     board = [["O","X","O","O","O","O","O","O","O"],["O","O","O","X","O","O","O","O","X"],["O","X","O","X","O","O","O","O","X"],["O","O","O","O","X","O","O","O","O"],["X","O","O","O","O","O","O","O","X"],["X","X","O","O","X","O","X","O","X"],["O","O","O","X","O","O","O","O","O"],["O","O","O","X","O","O","O","O","O"],["O","O","O","O","O","X","X","O","O"]]
#     board = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
#     pprint(board)
#     sol.solve(board)
#     print('after:')
#     pprint(board)
#     print('expected:')

