# Longest Common Prefix

from itertools import zip_longest

class Solution:
    def isHomogeneous(self, tup):
        if tup == ():
            return False

        first = tup[0]
        if first is None:
            return False

        return all(first == val for val in tup)

    def longestCommonPrefix(self, strs):
        zipped = zip_longest(*strs)
        prefix = ''
        for tup in zipped:
            if self.isHomogeneous(tup):
                prefix += tup[0]
            else:
                break

        return prefix

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
