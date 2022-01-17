# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        start = 0
        length = len(s)

        while start < length - longest:
            substr = s[start:start + longest + 1]
            if len(set(substr)) == longest + 1:
                longest += 1
            else:
                start += 1

        return longest

if __name__ == "__main__":
    sol = Solution()
    inp = ""
    print(sol.lengthOfLongestSubstring(inp))
