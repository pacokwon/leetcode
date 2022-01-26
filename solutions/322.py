# Coin Change

class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        for am in range(1, amount + 1):
            for c in coins:
                if c > am: continue
                dp[am] = min(dp[am - c] + 1, dp[am])

        return -1 if dp[amount] == float('inf') else dp[amount]

if __name__ == "__main__":
    sol = Solution()
    coins = [1]
    amount = 0
    print(sol.coinChange(coins, amount))
