# Coin Change 8
class Solution:
    def change(self, amount, coins):
        # Classic DP problem?

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for am in range(1, amount + 1):
                if am >= coin:
                    dp[am] += dp[am - coin]

        return dp[amount]

if __name__ == "__main__":
    sol = Solution()
    amount = 5
    coins = [1, 2, 5]
    print(sol.change(amount, coins))
