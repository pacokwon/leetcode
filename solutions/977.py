# Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums):
        return sorted([n * n for n in nums])
