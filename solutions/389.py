# Find The Difference

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ts = Counter(t)

        for ch, cnt in ts.items():
            if cnt != cs[ch]:
                return ch

        return ""

if __name__ == "__main__":
    sol = Solution()
    s = "abcd"
    t = "abcde"
    print( sol.findTheDifference(s, t) )
