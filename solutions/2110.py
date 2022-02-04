# Number of Smooth Descent Periods of a Stock

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # let's count the number of patches and
        # then we'll somehow mathematically calculate the result?

        index = 0
        length = len(prices)
        patches = []
        cnt = 1
        while index < length - 1:
            if prices[index] == prices[index + 1] + 1:
                cnt += 1
            else:
                # streak ended.
                if cnt > 0: patches.append(cnt)

                cnt = 1
            index += 1
        if cnt > 0:
            patches.append(cnt)

        # from a single patch arises many sub-patches.
        # for example, [3, 2, 1] has [3, 2], [2, 1], [3], [2], [1]
        # the number of sub-patches (including itself) can be calculated as 1 + 2 + 3 = 6
        return sum(n * (n + 1) // 2 for n in patches)

if __name__ == "__main__":
    sol = Solution()
    prices = [3,2,1,4]
    prices = [8,6,7,7]
    prices = [1]
    print(sol.getDescentPeriods(prices))
