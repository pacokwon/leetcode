from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_sum = sum(chalk)

        if k % chalk_sum == 0:
            return 0

        # leftover is larger than 0
        leftover = k - chalk_sum * (k // chalk_sum)

        for index, c in enumerate(chalk):
            if c > leftover:
                return index
            leftover -= c

        # unreachable
        return 0

# chalk = [9,9,9]
# k = 36
# print(Solution().chalkReplacer(chalk, k))
