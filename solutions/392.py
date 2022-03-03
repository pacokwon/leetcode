# Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sindex = 0
        for c in t:
            if sindex == len(s):
                break

            if c == s[sindex]:
                sindex += 1

        return sindex == len(s)

if __name__ == "__main__":
    sol = Solution()
    s = "abe"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
