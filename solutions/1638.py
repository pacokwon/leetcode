# Count Substrings That Differ by One Character

class Solution:
    def countSubstrings(self, s, t):
        # brute force
        slen = len(s)
        tlen = len(t)

        count = 0

        for si in range(slen):
            for ti in range(tlen):
                index = 0
                diffCount = 0
                while si + index < slen and ti + index < tlen:
                    if s[si + index] != t[ti + index]:
                        if diffCount == 1:
                            break

                        diffCount += 1

                    if diffCount == 1:
                        count += 1
                    index += 1

        return count

if __name__ == "__main__":
    sol = Solution()
    s = "abbab"
    t = "bbbbb"
    print(sol.countSubstrings(s, t))
