# House Robber II

class Solution:
    def helper(self, nums):
        length = len(nums)
        if length <= 2:
            return max(nums)

        # dp[index] is max cost for nums[index:]
        dp = [0] * length
        dp[length - 1] = nums[length - 1]
        dp[length - 2] = max(nums[length - 1], nums[length - 2])
        index = length - 3
        while index >= 0:
            dp[index] = max(nums[index] + dp[index + 2], dp[index + 1])
            index -= 1

        return max(dp[0], dp[1])

    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,2]
    nums = [1,2,3,1]
    nums = [1,2,3]
    nums = [1,3,1,3,100]
    print(sol.rob(nums))
