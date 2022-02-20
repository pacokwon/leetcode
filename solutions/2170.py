# Minimum Operations to Make the Array Alternating

from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        ec = Counter(nums[::2])
        oc = Counter(nums[1::2])

        eit = sorted(ec.items(), key=lambda x: -x[1])
        oit = sorted(oc.items(), key=lambda x: -x[1])

        even = eit[0]
        odd = oit[0]

        if even[0] == odd[0]:
            if len(oit) > 1:
                odd = oit[1]
            else:
                odd = (None, 0)

        oddCount = len(nums) // 2
        evenCount = len(nums) - oddCount

        return evenCount - even[1] + oddCount - odd[1]

if __name__ == "__main__":
    sol = Solution()
    nums = [3,1,3,2,4,3]
    nums = [1,2,2,2,2]
    nums = [2,2]
    nums = [1,1,1,1,1]
    print(sol.minimumOperations(nums))
