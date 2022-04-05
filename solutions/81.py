from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1

            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] <= nums[mid]:
                # left ~ right is sorted
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # not sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False

