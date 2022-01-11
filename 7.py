# Reverse Integer

class Solution:
    def reverse(self, x):
        if x < 0:
            isNegative = True
            x = -x
        else:
            isNegative = False

        rev = str(x)[::-1]
        length = len(rev)
        maxLength = 10 # length of 2147483648

        if isNegative:
            return 0 if length >= maxLength and rev > "2147483648" else -int(rev)
        else:
            return 0 if length >= maxLength and rev > "2147483647" else int(rev)


if __name__ == "__main__":
    sol = Solution()
    inp = -8463847412
    print(sol.reverse(inp))
