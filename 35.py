# Search Insert Position
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3]
    target = 0
    print(sol.searchInsert(nums, target))
