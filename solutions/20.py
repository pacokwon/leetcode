# Valid Parentheses

class Solution:
    def isOpening(self, c):
        return c == '(' or c == '{' or c == '['

    def matches(self, c1, c2):
        return (
            c1 == '(' and c2 == ')' or
            c1 == '{' and c2 == '}' or
            c1 == '[' and c2 == ']'
        )

    def isValid(self, s):
        stack = []
        for c in s:
            if self.isOpening(c):
                stack.append(c)
                continue

            # stack is empty on closing bracket encounter
            if not stack:
                return False

            top = stack.pop()
            if not self.matches(top, c):
                return False

        # True if empty. False otherwise
        return not bool(stack)

if __name__ == "__main__":
    sol = Solution()
    inp = "()]"
    print(sol.isValid(inp))
