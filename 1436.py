# Destination City
from collections import defaultdict

class Solution:
    def destCity(self, paths):
        hmap = defaultdict(bool)
        for [cityA, _] in paths:
            hmap[cityA] = True

        for [_, cityB] in paths:
            if not hmap[cityB]:
                return cityB

        raise ValueError("Invalid Test Case")

if __name__ == "__main__":
    sol = Solution()
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(sol.destCity(paths))
