# Count Elements With Strictly Smaller and Greater Elements

from typing import List

class Solution:
    def countElements(self, nums: List[int]) -> int:
        minel = min(nums)
        maxel = max(nums)

        ans = 0
        for n in nums:
            if minel < n < maxel:
                ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [15,15,13,13]
    print(sol.countElements(nums))
