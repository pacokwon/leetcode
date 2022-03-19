from typing import List
import heapq

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        hap = sum(nums)

        # the sum of reductions must be geq than this
        reduceLimit = hap / 2

        heap = [-float(n) for n in nums]
        heapq.heapify(heap)
        reduceHap = 0
        cnt = 0
        while reduceHap < reduceLimit:
            largest = -heap[0]
            reduceHap += largest / 2
            heapq.heapreplace(heap, -largest / 2)
            cnt += 1

        return cnt
