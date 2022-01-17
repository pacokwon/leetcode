# Find The Highest Altitude
from itertools import accumulate

class Solution:
    def largestAltitude(self, gain):
        return max(max(accumulate(gain)), 0)

if __name__ == "__main__":
    sol = Solution()
    inp = [-4,-3,-2,-1,4,3,2]
    print(sol.largestAltitude(inp))
