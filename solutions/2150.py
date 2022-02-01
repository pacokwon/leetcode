# Find All Lonely Elements in the Array

from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [n for n in nums if c[n + 1] + c[n - 1] + c[n] < 2]

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5,3]
    nums = [1,5,3]
    nums = [10,6,5,8]
    print(sol.findLonely(nums))
