# Search in a Rotated Sorted Array

class Solution:
    def findOffset(self, nums):
        left, right = 0, len(nums) - 1

        if len(nums) == 1 or nums[left] < nums[right]:
            return 0

        while left <= right:
            if left + 1 == right:
                return right

            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid

        return -1

    def search(self, nums, target):
        """
        2-step strategy:
            1. find the rotation offset in log(n)
            2. find the target in log(n)
        """

        offset = self.findOffset(nums)
        print(offset)

        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            val = nums[(offset + mid) % length]

            if val == target:
                return (offset + mid) % length
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    nums = [1]
    target = 1
    print(sol.search(nums, target))
