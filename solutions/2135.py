# Count Words Obtained After Adding a Letter
"""
attempted to use Counter, but resulted in a TLE
with the same approach with a bitmask
"""

from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start = set()
        for word in startWords:
            m = 0
            for c in word:
                m ^= 1 << (ord(c) - 97)
            start.add(m)

        ans = 0
        for word in targetWords:
            m = 0
            for c in word:
                m ^= 1 << (ord(c) - 97)

            for c in word:
                if m ^ (1 << (ord(c) - 97)) in start:
                    ans += 1
                    break
        return ans


if __name__ == "__main__":
    sol = Solution()
    startWords = ["ab","a"]
    targetWords = ["abc","abcd"]
    startWords = ["ant","act","tack"]
    targetWords = ["tack","act","acti"]
    print(sol.wordCount(startWords, targetWords))
