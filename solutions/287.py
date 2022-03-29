from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 6, 2, 4, 1, 7, 2, 5, 3, 2
        # 6 -> 5 -> 2 -> 4 -> 7 -> 3 -> 1 -> 2 ->
        #                ^
        slow, fast = nums[0], nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast: break

        slow = nums[0];
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow
