# All Divisions With the Highest Score of a Binary Array

from collections import Counter

class Solution:
    def maxScoreIndices(self, nums):
        cl = Counter()
        cr = Counter(nums)

        highest = cl[0] + cr[1]
        ans = [0]

        for index, n in enumerate(nums):
            cl[n] += 1
            cr[n] -= 1

            added = cl[0] + cr[1]
            if highest == added:
                ans.append(index + 1)
            elif highest < added:
                highest = added
                ans = [index + 1]

        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,0]
    nums = [1,1]
    print(sol.maxScoreIndices(nums))
