# Delete Operation for Two Strings

class Solution:
    def minDistance(self, word1, word2):
        len1, len2 = len(word1), len(word2)

        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

        for i in range(len1 + 1):
            dp[i][0] = i

        for j in range(len2 + 1):
            dp[0][j] = j

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[len1][len2]

if __name__ == "__main__":
    sol = Solution()
    word1 = "sea"
    word2 = "eat"

    word1 = "leetcode"
    word2 = "etco"

    word1 = "intention"
    word2 = "execution"

    print(sol.minDistance(word1, word2))
