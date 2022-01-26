# Combination Sum IV
class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target + 1)
        dp[0] = 1

        for t in range(1, target + 1):
            dp[t] = sum(0 if t - n < 0 else dp[t - n] for n in nums)

        return dp[target]

if __name__ == "__main__":
    sol = Solution()
    nums = [9]
    target = 3
    print(sol.combinationSum4(nums, target))
