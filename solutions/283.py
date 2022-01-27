# Move Zeroes

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        indices = []

        for index, n in enumerate(nums):
            if n != 0:
                indices.append(index)

        for i, nonZeroIndex in enumerate(indices):
            nums[i] = nums[nonZeroIndex]

        for i in range(len(indices), len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    sol = Solution()
    nums = [0]
    sol.moveZeroes(nums)
    print(nums)
