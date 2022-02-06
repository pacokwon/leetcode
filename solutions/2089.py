# Find Target Indices After Sorting Array

from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        return [index for index, val in enumerate(sorted(nums)) if val == target]

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,5,2,3]
    target = 2
    print( sol.targetIndices(nums, target) )
