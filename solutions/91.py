# Decode Ways

class Solution:
    def isValidTwoDigit(self, s):
        return '10' <= s <= '26'

    def isValidSingleDigit(self, s):
        return s != '0'

    def numDecodings(self, s):
        length = len(s)

        dp = [0] * (length + 1)

        # dp[i] stores how many decodings s[:i] has
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, length + 1):
            # last character of s[:i]
            if self.isValidTwoDigit(s[i-2:i]):
                dp[i] += dp[i - 2]

            if self.isValidSingleDigit(s[i - 1]):
                dp[i] += dp[i - 1]

        return dp[length]

if __name__ == "__main__":
    sol = Solution()
    inp = "06"
    print(sol.numDecodings(inp))
