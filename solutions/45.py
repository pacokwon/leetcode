# Jump Game II

class Solution:
    def jump(self, nums):
        length = len(nums)
        # we need a large initial value, and we know that length + 2 jumps cannot happen.
        dp = [length + 2] * length

        # already in destination. no jump necessary
        dp[length - 1] = 0

        index = length - 2
        while index >= 0:
            if nums[index] == 0:
                index -= 1
                continue

            farthest = min(index + nums[index], length - 1)
            dp[index] = 1 + min(dp[index + 1:farthest + 1])
            index -= 1

        return dp[0]

if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1,1,4]
    nums = [2,3,0,1,4]
    print(sol.jump(nums))
