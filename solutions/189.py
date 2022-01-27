# Rotate Array
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        if k == 0:
            return

        front = nums[length - k:]

        index = length - k - 1
        while index >= 0:
            nums[index + k] = nums[index]
            index -= 1

        for index, val in enumerate(front):
            nums[index] = val

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3

    nums = [-1,-100,3,99]
    k = 2

    nums = [1, 2]
    k = 2
    sol.rotate(nums, k)
    print(nums)
