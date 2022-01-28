# Find All Anagrams in a String

from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        slen, plen = len(s), len(p)
        if plen > slen:
            return []

        ans = []
        pstat = Counter(p)
        sstat = Counter(s[0:plen])
        if pstat == sstat:
            ans.append(0)

        si = 1
        while si <= slen - plen:
            sstat[s[si + plen - 1]] += 1
            sstat[s[si - 1]] -= 1
            if sstat[s[si - 1]] == 0:
                del sstat[s[si - 1]]

            if sstat == pstat:
                ans.append(si)
            si += 1

        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "cbaebabacd"
    p = "abc"

    # s = "abab"
    # p = "ab"
    print(sol.findAnagrams(s, p))
