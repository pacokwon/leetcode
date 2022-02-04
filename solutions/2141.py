# Maximum Running of N Computers

from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        length = len(batteries)
        if length < n:
            return 0

        batteries.sort()

        # get the n largest ones
        bt = batteries[-n:]

        # get the rest
        remaining = sum(batteries[:-n])

        added = 0
        for index, b in enumerate(bt):
            added += b
            if index + 1 < len(bt) and (added + remaining) // (index + 1) < bt[index + 1]:
                return (added + remaining) // (index + 1)

        return (added + remaining) // n

if __name__ == "__main__":
    sol = Solution()
    n = 3
    batteries = [4,3,2,1]
    print( sol.maxRunTime(n, batteries) )
