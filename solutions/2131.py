# Longest Palindrome by Concatenating Two Letter Words

from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs = 0
        sym = 0
        cnt = Counter()
        for word in words:
            rev = word[::-1]
            mirror = word == rev

            if cnt[rev] > 0:
                pairs += 1
                cnt[rev] -= 1
                sym -= 1 if mirror else 0
            else:
                cnt[word] += 1
                sym += 1 if mirror else 0

        return pairs * 4 + (2 if sym > 0 else 0)

# if __name__ == "__main__":
#     sol = Solution()
#     words = ["lc","cl","gg"]
#     words = ["ab","ty","yt","lc","cl","ab"]
#     words = ["cc","ll","xx"]
#     words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
#     print(sol.longestPalindrome(words))
