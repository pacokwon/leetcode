# K Radius Subarray Averages

from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        ans = [0] * length
        added = sum(nums[:k])

        for index, _ in enumerate(nums):
            if index <= k:
                if index + k >= length:
                    ans[index] = -1
                    continue

                added += nums[index + k]
                if index == k:
                    ans[index] = added // (2 * k + 1)
                else:
                    ans[index] = -1
            elif index >= length - k:
                ans[index] = -1
            else:
                added = added + nums[index + k] - nums[index - k - 1]
                ans[index] = added // (2 * k + 1)
        return ans

if __name__ == "__main__":
    sol = Solution()
    #       0 1 2 3 4 5 6 7 8
    nums = [7,4,3,9,1,8,5,2,6]
    k = 3
    nums = [1,2,3]
    k = 3
    nums = [8]
    k = 10000
    print(sol.getAverages(nums, k))
