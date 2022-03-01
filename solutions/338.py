# Counting Bits

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [None] * (n + 1)

        ans[0] = 0
        for i in range(1, n + 1):
            cnt = 0
            m = i
            while m != 0:
                m = m & (m - 1)
                cnt += 1
            ans[i] = cnt

        return ans

if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.countBits(n))
