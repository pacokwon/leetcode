# Check if Every Row and Column Contains All Numbers

from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for r in range(n):
            visited = [False] * n

            for c in range(n):
                if visited[matrix[r][c] - 1]:
                    return False

                visited[matrix[r][c] - 1] = True


        for c in range(n):
            visited = [False] * n

            for r in range(n):
                if visited[matrix[r][c] - 1]:
                    return False

                visited[matrix[r][c] - 1] = True

        return True

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    matrix = [[1,1,1],[1,2,3],[1,2,3]]
    print(sol.checkValid(matrix))
