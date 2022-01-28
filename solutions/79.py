# Word Search

class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        length = len(word)

        def helper(r, c, wordIndex):
            # assumes that (r, c) contains the letter, so not checking
            visited[r][c] = True

            nextLetter = word[wordIndex + 1]
            for _dx, _dy in zip(dx, dy):
                nr = r + _dx
                nc = c + _dy

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if visited[nr][nc] or board[nr][nc] != nextLetter:
                    continue

                if wordIndex + 1 == length - 1:
                    return True

                if helper(nr, nc, wordIndex + 1):
                    return True

            visited[r][c] = False
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if length == 1:
                        return True

                    if helper(r, c, 0):
                        return True

        return False

if __name__ == "__main__":
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "A"

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    print(sol.exist(board, word))
