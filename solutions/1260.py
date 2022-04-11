from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flattened = sum(grid, [])
        n = len(flattened)
        rows = len(grid)
        cols = len(grid[0])
        k = k % n
        return [[flattened[(-k + cols * r + c + n) % n]  for c in range(cols)] for r in range(rows)]

if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
    k = 4
    grid = [[1],[2],[3],[4],[7],[6],[5]]
    k = 2
    print(Solution().shiftGrid(grid, k))
