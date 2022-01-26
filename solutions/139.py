# Word Break

class Solution:
    def wordBreak(self, s, wordDict):
        setDict = set(wordDict) # faster lookup time
        length = len(s)
        dp = [True] * (length + 1)
        for index in range(1, length + 1):
            dp[index] = any(dp[l] and s[l:index] in setDict for l in range(index))

        return dp[length]

if __name__ == "__main__":
    sol = Solution()
    # s = "leetcode"
    # wordDict = ["leet","code"]

    s = "applepenapple"
    wordDict = ["apple","pen"]

    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]

    s = "aaaaaaa"
    wordDict = ["aaaa","aaa"]
    print(sol.wordBreak(s, wordDict))
