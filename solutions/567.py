# Permutation in String

from collections import Counter

class Solution:
    def checkInclusion(self, s1, s2):
        stat = Counter(s1)
        length1 = len(s1)
        length2 = len(s2)

        index = 0
        while index <= length2 - length1:
            # stat of substring
            substrStat = Counter(s2[index:index+length1])
            if substrStat == stat:
                return True
            index += 1

        return False

if __name__ == "__main__":
    sol = Solution()
    s1 = "adc"
    s2 = "dcda"
    print(sol.checkInclusion(s1, s2))
