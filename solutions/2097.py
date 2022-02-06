
from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int) # net out degree
        for x, y in pairs:
            graph[x].append(y)
            degree[x] += 1
            degree[y] -= 1

        for k in degree:
            if degree[k] == 1:
                x = k
                break

        ans = []

        def fn(x):
            """Return Eulerian path via dfs."""
            print(x, graph[x])
            while graph[x]: fn(graph[x].pop())
            ans.append(x)

        fn(x)
        print(ans)
        ans.reverse()
        return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]

if __name__ == "__main__":
    sol = Solution()
    pairs = [[1, 2], [1, 3], [2, 1]]
    print( sol.validArrangement(pairs) )
