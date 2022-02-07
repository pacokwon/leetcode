# Remove Duplicates from Sorted Array II

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        length = len(nums)
        k = 0

        while index < length:
            val = nums[index]
            count = 0
            while index < length and val == nums[index]:
                count += 1
                index += 1

            k += min(count, 2)
            if count <= 2:
                continue

            mvi = index
            while mvi < length:
                nums[mvi - count + 2] = nums[mvi]
                mvi += 1

            index = index - count + 2
            length -= count - 2
        return k

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    nums = [0,1,2,3]
    k = sol.removeDuplicates(nums)
    print(nums[:k])
