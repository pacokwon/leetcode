# Bitwise AND of Numbers Range
# I'm not a wizard, and this is a long solution

import math

class Solution:
    def rangeBitwiseAnd(self, left, right):
        if left == 0 or right == 0:
            return 0

        if left == right:
            return left

        if left + 1 == right:
            return left & right

        # compute their "zone"s
        # zones are number of bits, considering the MSB is the leftmost
        zl = math.floor(math.log2(left))
        zr = math.floor(math.log2(right))

        # if zones are different, then it's zero
        if zl != zr:
            return 0

        diff = right - left
        zone = math.floor(math.log2(diff))
        pow = 2 ** (zone + 1)

        higher = self.rangeBitwiseAnd(left // pow, right // pow) << (zone + 1)

        return higher


if __name__ == "__main__":
    sol = Solution()
    left = 1
    right = 2147483647

    left  = 0b10111
    right = 0b11001

    left  = 0b11011001
    right = 0b11100000
    print(sol.rangeBitwiseAnd(left, right))
