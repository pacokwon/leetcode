# Detonate the Maximum Bombs

from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        length = len(bombs)
        reachable = [[False] * length for _ in range(length)]

        for i in range(length):
            for j in range(i + 1, length):
                [x1, y1, r1] = bombs[i]
                [x2, y2, r2] = bombs[j]

                dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
                reachable[i][j] = r1 ** 2 >= dist
                reachable[j][i] = r2 ** 2 >= dist

        def dfs(start, visited):
            for index, r in enumerate(reachable[start]):
                if r and index not in visited:
                    visited.add(index)
                    dfs(index, visited)

        ans = 0
        for i in range(length):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
        return ans

if __name__ == "__main__":
    sol = Solution()
    bombs = [[2,1,3],[6,1,4]]
    bombs = [[1,1,5],[10,10,5]]
    bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    print( sol.maximumDetonation(bombs) )
