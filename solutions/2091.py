# Removing Minimum and Maximum From Array

from typing import List, Tuple

class Solution:
    def getMinMaxIndices(self, nums: List[int]) -> Tuple[int, int]:
        mn = 0
        mx = 0
        for index, val in enumerate(nums):
            if val > nums[mx]:
                mx = index

            if val < nums[mn]:
                mn = index

        return mx, mn

    def minimumDeletions(self, nums: List[int]) -> int:
        length = len(nums)
        mx, mn = self.getMinMaxIndices(nums)

        # distance from left is defined as {index + 1}
        # distance from right is defined as {length - index}
        mxLeft, mxRight = mx + 1, length - mx
        mxShortDist = min(mxLeft, mxRight)

        mnLeft, mnRight = mn + 1, length - mn
        mnShortDist = min(mnLeft, mnRight)
        print(mx, mn)
        print(mxShortDist, mnShortDist)

        if mx == mn:
            # doesn't matter which, just pop once and we're done
            return mxShortDist

        # pop the shorter one first
        if mxShortDist < mnShortDist:
            if mxShortDist == mxLeft:
                mn -= mx + 1
                length -= mx + 1
            else:
                length = mx
            return mxShortDist + min(mn + 1, length - mn)
        else:
            if mnShortDist == mnLeft:
                mx -= mn + 1
                length -= mn + 1
            else:
                length = mn
            return mnShortDist + min(mx + 1, length - mx)

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,10,7,5,4,1,6]
    nums = [0,-4,19,1,8,-2,-3,5]
    nums = [1,1,1,101,2,2,2,3,4]
    nums = [-87,60,-30,-67,74,55,76,-53]
    print(sol.minimumDeletions(nums))
