class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        # starting at level 1. level 1's score is 0.
        stack.append(0)

        index = 0
        while index < len(s):
            c = s[index]

            if c == '(':
                # increase level
                stack.append(0)
            else:
                # decrease level
                top = stack.pop()
                if top == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += top * 2

            index += 1

        return stack[-1]

if __name__ == "__main__":
    sol = Solution()
    s = "()"
    s = "(())"
    s = "((()))((()))"
    print(sol.scoreOfParentheses(s))
