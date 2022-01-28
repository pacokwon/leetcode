# Find First and Last Position of Element in Sorted Array

class Solution:
    def binSearch(self, nums, target):
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                while mid >= 0 and nums[mid] == target:
                    mid -= 1
                return mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


    def searchRange(self, nums, target):
        found = self.binSearch(nums, target)
        if found == -1:
            return [-1, -1]

        start = found
        while found < len(nums) and nums[found] == target:
            found += 1

        return [start, found - 1]

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1]
    target = 1
    print(sol.searchRange(nums, target))
