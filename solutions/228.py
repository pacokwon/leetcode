# Summary Ranges

from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        index = 0
        while index < len(nums):
            start = index
            val = nums[index]
            index += 1
            while index < len(nums) and val + 1 == nums[index]:
                val = nums[index]
                index += 1

            # start to index
            if start + 1 == index:
                ans.append(str(nums[start]))
            else:
                ans.append(f"{nums[start]}->{nums[index - 1]}")
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,2,4,5,7]
    nums = [0,2,3,4,6,8,9]
    nums = [0]
    nums = [0,1]
    print(sol.summaryRanges(nums))
