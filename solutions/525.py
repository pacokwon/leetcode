# Contiguous Array

from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        tracker = {}
        tracker[0] = 0

        ans = 0
        added = 0
        for index, n in enumerate(nums):
            added += 2 * n - 1 # 0 -> -1, 1 -> 1

            if added in tracker:
                ans = max(ans, index + 1 - tracker[added])
            else:
                tracker[added] = index + 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,1,0,1,0,0]
    nums = [0,1,0]
    print(sol.findMaxLength(nums))
