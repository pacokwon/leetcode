from itertools import groupby
from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def group(word):
            return [(val, len(list(lst))) for val, lst in groupby(word)]

        def extendable(s, word):
            if len(s) != len(word):
                return False

            index = 0
            while index < len(s):
                sval, scount = s[index]
                wval, wcount = word[index]

                # character orderings don't match
                if sval != wval:
                    return False

                # word has more characters
                if wcount > scount:
                    return False

                if not (wcount == scount or scount >= 3):
                    return False

                index += 1

            return True

        sGrouped = group(s)
        wordsGrouped = [group(w) for w in words]

        ans = 0
        for w in wordsGrouped:
            if extendable(sGrouped, w):
                ans += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    s = "zzzzzyyyyy"
    words = ["zzyy","zy","zyy"]
    print(sol.expressiveWords(s, words))
