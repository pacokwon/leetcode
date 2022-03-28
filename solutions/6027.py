from typing import List
from itertools import groupby

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        grouped = [(c, len(list(l))) for c, l in groupby(nums)]

        if len(grouped) <= 2:
            return 0

        ans = 0
        index = 1
        while index < len(grouped) - 1:
            if grouped[index - 1][0] <= grouped[index][0] and grouped[index][0] >= grouped[index + 1][0]:
                ans += 1
            elif grouped[index - 1][0] >= grouped[index][0] and grouped[index][0] <= grouped[index + 1][0]:
                ans += 1
            index += 1

        return ans
