# Number Of Boomerangs
from collections import defaultdict

class Solution:
    def choose(self, n, r):
        res = 1
        for ri in range(r):
            res = res * (n - ri) // (ri + 1)

        return res

    def numberOfBoomerangs(self, points):
        if len(points) <= 2:
            return 0

        dists = [defaultdict(int) for _ in points]
        for i, [x1, y1] in enumerate(points):
            j = i + 1
            while j < len(points):
                [x2, y2] = points[j]
                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dists[i][distance] += 1
                dists[j][distance] += 1
                j += 1

        ans = 0
        for ddct in dists:
            for key in ddct:
                count = ddct[key]
                ans += count * (count - 1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    # inp = [[0,0],[1,0],[2,0]]
    inp = [[1,1]]
    print(sol.numberOfBoomerangs(inp))
    # print(sol.choose(5, 2))
