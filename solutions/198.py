# House Robber

class Solution:
    def rob(self, nums):
        length = len(nums)
        if length == 1:
            return nums[0]

        dp = [-1] * len(nums)

        index = length - 1
        while index >= 0:
            num = nums[index]

            if index == length - 1:
                dp[index] = num
            elif index == length - 2:
                dp[index] = max(num, dp[index + 1])
            else:
                dp[index] = max(dp[index + 1], num + dp[index + 2])

            index -= 1

        return max(dp[0], dp[1])

if __name__ == "__main__":
    sol = Solution()
    inp = [1, 2, 3, 1]
    inp = [2, 7, 9, 3, 1]
    print(sol.rob(inp))
