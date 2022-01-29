# LCS

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        len1, len2 = len(text1), len(text2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i1 in range(len1):
            for i2 in range(len2):
                dp[i1 + 1][i2 + 1] = 1 + dp[i1][i2] if text1[i1] == text2[i2] else max(dp[i1][i2 + 1], dp[i1 + 1][i2])

        return dp[len1][len2]

if __name__ == "__main__":
    sol = Solution()
    text1 = "abc"
    text2 = "def"
    print(sol.longestCommonSubsequence(text1, text2))
