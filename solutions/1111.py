# Maximum Nesting Depth of Two Valid Parentheses Strings

class Solution:
    def computeMaxDepth(self, seq):
        depth = 0
        maxDepth = 0
        for c in seq:
            if c == '(':
                depth += 1
                maxDepth = max(maxDepth, depth)
            else:
                depth -= 1
        return maxDepth

    def attemptSplit(self, seq, threshold):
        depth = 0
        ans = [0] * len(seq)
        for index, c in enumerate(seq):
            if c == '(':
                depth += 1
                if depth > threshold:
                    ans[index] = 1
            else:
                if depth > threshold:
                    ans[index] = 1
                depth -= 1

        return ans


    def maxDepthAfterSplit(self, seq):
        maxDepth = self.computeMaxDepth(seq)
        return self.attemptSplit(seq, maxDepth // 2)

if __name__ == "__main__":
    sol = Solution()
    # inp = "()(())()"
    inp = "(()())"
    print(sol.maxDepthAfterSplit(inp))
