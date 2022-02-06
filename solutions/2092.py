# Find All People With Secret

from typing import List
from itertools import groupby
from collections import defaultdict
from queue import Queue

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        hasSecret = { 0, firstPerson }

        for time, pts in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            edges = defaultdict(list)
            q = Queue()
            for [a, b, _] in pts:
                edges[a].append(b)
                edges[b].append(a)
                if a in hasSecret:
                    q.put(a)
                if b  in hasSecret:
                    q.put(b)

            while not q.empty():
                v = q.get()
                for u in edges[v]:
                    if u not in hasSecret:
                        hasSecret.add(u)
                        q.put(u)
        return list(hasSecret)

# if __name__ == "__main__":
#     sol = Solution()
#     n = 11
#     meetings = [[5,1,4],[0,4,18]]
#     firstPerson = 1
#     # expected: [0,1,4,5]
#     print( sol.findAllPeople(n, meetings, firstPerson) )
