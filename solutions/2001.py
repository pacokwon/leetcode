# Number of Pairs of Interchangeable Rectangles

from typing import List
from collections import defaultdict

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hm = defaultdict(int)
        for [w, h] in rectangles:
            hm[w / h] += 1

        ans = 0
        for _, val in hm.items():
            ans += val * (val - 1) // 2

        return ans

if __name__ == "__main__":
    sol = Solution()
    rectangles = [[4,8],[3,6],[10,20],[15,30]]
    print(sol.interchangeableRectangles(rectangles))
