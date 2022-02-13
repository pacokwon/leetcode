# Find N Unique Integers Up to Zero

from typing import List
import itertools

class Solution:
    def sumZero(self, n: int) -> List[int]:
        half = n // 2
        res = list(itertools.chain(range(-half, 0), range(1, half + 1)))
        if n % 2 == 1:
            res.append(0)

        return res

if __name__ == "__main__":
    sol = Solution()
    n = 1
    print(sol.sumZero(n))
