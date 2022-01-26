# Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        # DP. let DP[i] be the largest sum that contains the ith element
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for index, val in enumerate(nums):
            if index == 0: continue

            added = dp[index - 1] + val

            if added > val:
                dp[index] = added
            else:
                dp[index] = val

        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    nums = [5,4,-1,7,8]
    print(sol.maxSubArray(nums))
