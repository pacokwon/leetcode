# Find Subsequence of Length K With the Largest Sum

from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        withIndex = list(enumerate(nums))
        withIndex.sort(key=lambda x: x[1])
        return [nums[index] for index, _ in sorted(withIndex[-k:])]

if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,3,3]
    nums = [-2, -3, 1, 4]
    k = 3
    nums = [50, -75]
    k = 2
    print(sol.maxSubsequence(nums, k))
