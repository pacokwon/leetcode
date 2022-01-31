# Spiral Matrix

class Solution:
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        ans = [0] * (rows * cols)
        r = 0
        c = -1
        count = 0
        d = 1

        while True:
            for _ in range(cols):
                c += d
                ans[count] = matrix[r][c]
                count += 1
            cols -= 1
            if count == len(ans):
                break

            for _ in range(rows - 1):
                r += d
                ans[count] = matrix[r][c]
                count += 1
            rows -= 1
            if count == len(ans):
                break

            d = -d

        return ans

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sol.spiralOrder(matrix))
