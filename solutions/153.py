# Find Minimum in a Rotated Array

class Solution:
    def findMin(self, nums):
        length = len(nums)
        left, right = 0, length - 1
        if length == 1 or nums[left] < nums[right]:
            return nums[0]

        while left < right:
            if left + 1 == right:
                return nums[right]

            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid

        return -1

if __name__ == "__main__":
    sol = Solution()
    nums = [3,4,5,1,2]
    nums = [4,5,6,7,0,1,2]
    nums = [11,13,15,17]
    print(sol.findMin(nums))
