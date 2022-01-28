# Generate Parentheses

class Solution:
    def generateParenthesis(self, n):
        length = 2 * n
        path = [None] * length

        """
        openUsedCount: how many opening braces did we use in TOTAL
        openCount: how many opening braces are not closed yet
        count: the current length of `path`
        """
        def helper(openUsedCount, openCount, count, path, ans):
            if count == length:
                ans.append(''.join(path))
                return

            if openUsedCount < n:
                path[count] = '('
                helper(openUsedCount + 1, openCount + 1, count + 1, path, ans)

            if openCount > 0:
                path[count] = ')'
                helper(openUsedCount, openCount - 1, count + 1, path, ans)

        ans = []
        helper(0, 0, 0, path, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(2))
