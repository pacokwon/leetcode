# Execution of All Suffix Instructions Staying in a Grid

from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        [sx, sy] = startPos
        dir = {
            "U": [-1, 0],
            "R": [0, 1],
            "D": [1, 0],
            "L": [0, -1],
        }
        ans = []
        for i, _ in enumerate(s):
            x, y = sx, sy
            j = i

            while j < len(s):
                dx, dy = dir[s[j]]
                x += dx
                y += dy

                if not (0 <= x and x < n and 0 <= y and y < n):
                    break

                j += 1

            ans.append(j - i)

        return ans

if __name__ == "__main__":
    sol = Solution()
    n = 3
    startPos = [0,1]
    s = "RRDDLU"
    print(sol.executeInstructions(n, startPos, s))
