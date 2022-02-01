# Number of Laser Beams in a Bank

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0

        def countOne(row):
            ans = 0
            for c in row:
                if c == '1':
                    ans += 1
            return ans

        ans = 0
        nums = [countOne(row) for row in bank]
        index = 0
        while index < len(nums) - 1:
            next = index + 1
            while next < len(nums) and nums[next] == 0:
                next += 1

            if next == len(nums):
                break

            ans += nums[index] * nums[next]
            index = next

        return ans
