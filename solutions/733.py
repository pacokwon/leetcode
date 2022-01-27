# Flood Fill

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        rows = len(image)
        cols = len(image[0])
        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        targetColor = image[sr][sc]

        # missed this corner case
        if targetColor == newColor:
            return image

        def fill(r, c):
            image[r][c] = newColor
            print(r, c)

            for _dx, _dy in zip(dx, dy):
                newR = r + _dx
                newC = c + _dy

                if not (0 <= newR < rows and 0 <= newC < cols):
                    continue

                if image[newR][newC] != targetColor:
                    continue

                fill(newR, newC)

        fill(sr, sc)
        return image

if __name__ == "__main__":
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2

    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2

    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 1

    print(sol.floodFill(image, sr, sc, newColor))
