# Maximum Fruits Harvested After at Most K Steps

from typing import List
import itertools

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        maxPos = max(startPos, fruits[-1][0])
        fruitMap = [0] * (maxPos + 2)
        for f in fruits:
            fruitMap[f[0]] = f[1]

        psum = [0] + list(itertools.accumulate(fruitMap))

        ans = 0
        # go right first
        for dist in range(k + 1):
            rightEnd = startPos + dist
            if rightEnd > maxPos or fruitMap[rightEnd] == 0: continue

            leftDist = max(0, k - dist * 2)
            leftEnd = max(0, startPos - leftDist)
            ans = max(ans, psum[rightEnd + 1] - psum[leftEnd])

        for dist in range(k + 1):
            leftEnd = startPos - dist
            if leftEnd < 0 or fruitMap[leftEnd] == 0: continue

            rightDist = max(0, k - dist * 2)
            rightEnd = min(maxPos, startPos + rightDist)
            ans = max(ans, psum[rightEnd + 1] - psum[leftEnd])

        return ans

if __name__ == "__main__":
    sol = Solution()
    fruits = [[2,8],[6,3],[8,6]]
    startPos = 5
    k = 4
    fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
    startPos = 5
    k = 4
    fruits = [[0,3],[6,4],[8,5]]
    startPos = 3
    k = 2
    print(sol.maxTotalFruits(fruits, startPos, k))
