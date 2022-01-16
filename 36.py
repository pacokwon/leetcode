# Valid Sduoku
class Solution:
    def bitmapCheck(self, bitmap, pos):
        return bitmap & (1 << (9 - pos)) != 0

    def bitmapSet(self, bitmap, pos):
        return bitmap | (1 << (9 - pos))

    def checkRows(self, board):
        for r in range(9):
            if not self.checkRow(board, r):
                return False

        return True

    def checkRow(self, board, rowNum):
        row = board[rowNum]
        bitmap = 0
        for n in row:
            if n == -1: continue

            if self.bitmapCheck(bitmap, n):
                return False

            bitmap = self.bitmapSet(bitmap, n)

        return True

    def transpose(self, board):
        rows = len(board)
        cols = len(board[0])
        return [[board[c][r] for c in range(cols)] for r in range(rows)]

    def gridToRow(self, board, r, c):
        mr = 3 * r
        mc = 3 * c
        return [board[mr + i][mc + j] for i in range(3) for j in range(3)]

    def gridsToRows(self, board):
        return [self.gridToRow(board, r, c) for r in range(3) for c in range(3)]

    def isValidSudoku(self, board):
        intBoard = [[-1 if c == '.' else int(c) for c in row] for row in board]

        colVersion = self.transpose(intBoard)
        gridVersion = self.gridsToRows(intBoard)

        return self.checkRows(intBoard) and self.checkRows(colVersion) and self.checkRows(gridVersion)

if __name__ == "__main__":
    sol = Solution()
    inp = [["8","3",".",".","7",".",".",".","."]
          ,["6",".",".","1","9","5",".",".","."]
          ,[".","9","8",".",".",".",".","6","."]
          ,["8",".",".",".","6",".",".",".","3"]
          ,["4",".",".","8",".","3",".",".","1"]
          ,["7",".",".",".","2",".",".",".","6"]
          ,[".","6",".",".",".",".","2","8","."]
          ,[".",".",".","4","1","9",".",".","5"]
          ,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(inp))
