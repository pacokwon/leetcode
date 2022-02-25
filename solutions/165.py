# Compare Version Numbers

from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vs1 = [int(v) for v in version1.split(".")]
        vs2 = [int(v) for v in version2.split(".")]

        for v1, v2 in zip_longest(vs1, vs2, fillvalue=0):
            if v1 == v2:
                continue

            if v1 > v2:
                return 1
            else:
                return -1

        return 0

if __name__ == "__main__":
    sol = Solution()
    version1 = "0.1"
    version2 = "1.1"
    print(sol.compareVersion(version1, version2))
