# Integer Break

class Solution:
    def integerBreak(self, n):
        dp = [0] * (max(7, n + 1))
        dp[2] = 1
        dp[3] = 2
        dp[4] = 4
        dp[5] = 6
        dp[6] = 9

        if n <= 6:
            return dp[n]

        mod = n % 3
        if mod == 0:
            return dp[6] * 3 ** ((n - 6) // 3)
        elif mod == 1:
            return dp[4] * 3 ** ((n - 4) // 3)
        else:
            return dp[5] * 3 ** ((n - 5) // 3)

if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.integerBreak(n))
