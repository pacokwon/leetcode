# Triangle

class Solution:
    def minimumTotal(self, triangle):
        length = len(triangle)
        for row in range(1, length):
            for col in range(row + 1):
                if col == 0:
                    triangle[row][0] += triangle[row - 1][0]
                elif col == row:
                    triangle[row][row] += triangle[row - 1][row - 1]
                else:
                    triangle[row][col] += min(triangle[row - 1][col], triangle[row - 1][col - 1])

        return min(triangle[length - 1])


if __name__ == "__main__":
    sol = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    triangle = [[-10]]
    print(sol.minimumTotal(triangle))
