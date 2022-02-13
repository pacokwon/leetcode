# Maximum Number of Eaten Apples

from typing import List
import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        hp = []
        ans = 0
        for index, app in enumerate(apples):
            heapq.heappush(hp, (index + days[index], app))

            d, cnt = heapq.heappop(hp)
            while d < index:
                d, cnt = heapq.heappop(hp)

            ans += 1

            if d > index:
                heapq.heappush(hp, (d, cnt - 1))
