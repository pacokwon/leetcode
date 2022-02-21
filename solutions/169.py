from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        half = n // 2
        for k, v in c.items():
            if v > half:
                return k
        return 0

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,3]
    # nums = [2,2,1,1,1,2,2]
    print(sol.majorityElement(nums))
