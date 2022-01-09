# Implement strstr

class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        # small optimization
        hLen = len(haystack)
        nLen = len(needle)
        index = 0
        while index <= hLen - nLen:
            substr = haystack[index:index + nLen]
            if substr == needle:
                return index
            index += 1

        return -1

if __name__ == "__main__":
    sol = Solution()
    haystack = "hello"
    needle = "ll"
    print(sol.strStr(haystack, needle))
