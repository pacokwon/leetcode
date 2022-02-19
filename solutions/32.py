# Longest Valid Parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        starting = {}

        ans = 0
        starting[0] = -1
        stack = 0

        for index, c in enumerate(s):
            if c == '(':
                stack += 1
                starting[stack] = index
            else:
                stack -= 1
                if stack in starting:
                    ans = max(ans, index - starting[stack])
                else:
                    starting[stack] = index

        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "(()"
    s = ")()())"
    s = ""
    print(sol.longestValidParentheses(s))
