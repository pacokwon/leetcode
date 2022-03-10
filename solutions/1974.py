# Minimum Time to Type Word Using Special Typewriter

class Solution:
    def minTimeToType(self, word: str) -> int:
        def diff(c1, c2):
            a1 = ord(c1)
            a2 = ord(c2)

            return min(abs(a2 - a1), 26 - abs(a2 - a1))

        ans = len(word) + diff('a', word[0])
        for i in range(1, len(word)):
            ans += diff(word[i - 1], word[i])
        return ans
