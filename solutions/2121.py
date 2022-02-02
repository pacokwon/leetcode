# Intervals Between Identical Elements

from typing import List
from collections import defaultdict

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        indices = defaultdict(list)
        for index, n in enumerate(arr):
            indices[n].append(index)

        ans = [0] * len(arr)

        for _, inds in indices.items():
            ps = [0] * len(inds)

            for ith, ind in enumerate(inds):
                if ith == 0:
                    ps[0] = ind
                else:
                    ps[ith] = ps[ith - 1] + ind

            for ith, ind in enumerate(inds):
                ans[ind] = abs((ith + 1) * ind - ps[ith]) + abs((len(inds) - 1 - ith) * ind - (ps[len(inds) - 1] - ps[ith]))

        return ans

if __name__ == "__main__":
    sol = Solution()
    arr = [2,1,3,1,2,3,3]
    arr = [10,5,10,10]
    print(sol.getDistances(arr))
