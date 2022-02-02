# Recover the Original Array

from typing import List
from collections import Counter
from copy import deepcopy

class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        blueprint = Counter(nums)

        def check(k, blueprint):
            cnt = deepcopy(blueprint)
            ans = []
            for n in nums:
                if cnt[n] == 0:
                    continue
                if cnt[n + k] == 0:
                    return False, []

                cnt[n] -= 1
                cnt[n + k] -= 1
                ans.append(n + k // 2)

            return True, ans

        ks = []
        for i in range(1, len(nums)):
            k = nums[i] - nums[0]
            if k != 0 and k % 2 == 0:
                ks.append(k)

        for k in ks:
            valid, ans = check(k, blueprint)
            if valid:
                return ans

        return []

if __name__ == "__main__":
    sol = Solution()
    nums = [2,10,6,4,8,12]
    print(sol.recoverArray(nums))
