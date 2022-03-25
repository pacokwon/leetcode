from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        first = [f for f, _ in costs]
        diff = [s - f for f, s in costs]
        return sum(first) + sum(sorted(diff)[:n])
