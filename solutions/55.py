# Jump Game

class Solution:
    def canJump(self, nums):
        length = len(nums)
        dest = length - 1
        index = length - 2
        while index >= 0:
            if nums[index] + index >= dest:
                dest = index

            index -= 1

        return dest == 0

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))
