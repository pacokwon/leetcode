# Richest Customer Wealth

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)

if __name__ == "__main__":
    sol = Solution()
    accounts = [[1,2,3],[3,2,1]]
    print(sol.maximumWealth(accounts))
