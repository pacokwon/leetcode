# Minimum Swaps to Group All 1's Together II

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        window = nums.count(1)
        length = len(nums)

        maxOnes = 0
        for i in range(window):
            if nums[i] == 1:
                maxOnes += 1

        cnt = maxOnes
        for i in range(1, length):
            new = nums[(i + window - 1) % length]
            old = nums[i - 1]

            cnt = cnt + new - old
            maxOnes = max(cnt, maxOnes)

        return window - maxOnes

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,1,1,0,0,1,1,0]
    print(sol.minSwaps(nums))
