# Rearrange Array Elements by Sign

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        copied = nums[:]

        pos = 0
        neg = 0
        for index, n in enumerate(copied):
            if n > 0:
                nums[pos * 2] = copied[index]
                pos += 1
            else:
                nums[neg * 2 + 1] = copied[index]
                neg += 1

        return nums

if __name__ == "__main__":
    sol = Solution()
    nums = [3,1,-2,-5,2,-4]
    nums = [-1,1]
    print(sol.rearrangeArray(nums))
