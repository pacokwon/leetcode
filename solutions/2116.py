# Check if a Parentheses String Can Be Valid

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        def validate(s: str, locked: str, p: str) -> bool:
            stack = 0
            free = 0
            for index, c in enumerate(s):
                if locked[index] == '1':
                    stack += 1 if c == p else -1
                else:
                    free += 1

                if stack + free < 0:
                    return False

            return free >= stack

        return validate(s, locked, '(') and validate(s[::-1], locked[::-1], ')')

# if __name__ == "__main__":
#     sol = Solution()
#     s      = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
#     locked = "100011110110011011010111100111011101111110000101001101001111"

#     s      = "())()))()(()(((())(()()))))((((()())(())"
#     locked = "1011101100010001001011000000110010100101"
#     print(sol.canBeValid(s, locked))
