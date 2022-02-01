# The Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, maxi = -1, -1

        ans = 0
        for index, p in enumerate(prices):
            if mini == -1:
                mini = index
            elif p < prices[mini]:
                mini = index
                maxi = -1

            if maxi == -1:
                maxi = index
            elif p > prices[maxi]:
                maxi = index
                ans = max(ans, prices[maxi] - prices[mini])

        return ans

if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    prices = [7,6,4,3,1]
    prices = [2,4,1]
    print(sol.maxProfit(prices))
