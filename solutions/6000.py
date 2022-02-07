
from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = sorted(nums[::2])
        odd = sorted(nums[1::2], reverse=True)
        for index, v in enumerate(even):
            nums[index * 2] = v
        for index, v in enumerate(odd):
            nums[index * 2 + 1] = v
        return nums

if __name__ == "__main__":
    sol = Solution()
    nums = [4,1,2,3]
    print(sol.sortEvenOdd(nums))
