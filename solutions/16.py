# 3 Sum Closest

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = None
        for i in range(len(nums) - 2):
            # new target
            t = target - nums[i]

            # i + 1 ~ len(nums) - 1

            left = i + 1
            right = len(nums) - 1

            while left < right:
                added = nums[left] + nums[right]
                if ans is None:
                    ans = added + nums[i]
                else:
                    ans = (added + nums[i]) if abs(t - added) < abs(target - ans) else ans

                if added == t:
                    ans = target
                    return target
                elif added < t:
                    left += 1
                else:
                    right -= 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1

    nums = [0,0,0]
    target = 1
    print(sol.threeSumClosest(nums, target))
