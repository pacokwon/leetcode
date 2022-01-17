# Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        # make 2d array
        dp = [[False] * length for _ in range(length)]
        ans = s[0]

        # initialize dp for length 1
        for i in range(length):
            dp[i][i] = True

        # initialize dp for length 2
        for i in range(length - 1):
            dp[i][i + 1] = s[i] == s[i + 1]

            if dp[i][i + 1]:
                ans = s[i:i+2]

        # for substrings of length [3, length]
        for l in range(3, length + 1):
            for index in range(length - l + 1):
                start = index
                end = index + l - 1
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    ans = s[start:end+1]
                    dp[start][end] = True

        return ans


if __name__ == "__main__":
    sol = Solution()
    inp = "cbbd"
    print(sol.longestPalindrome(inp))
