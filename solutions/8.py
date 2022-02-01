# String to Integer

class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        while index < len(s) and s[index] == ' ':
            index += 1

        if index == len(s):
            return 0

        negative = False
        negMax = 2 ** 31
        posMax = 2 ** 31 - 1
        # there is a character on index now
        if s[index] == '+':
            negative = False
            index += 1
        elif s[index] == '-':
            negative = True
            index += 1

        # there should be a digit on index now
        start = index
        while index < len(s) and '0' <= s[index] <= '9':
            index += 1

        digitPart = s[start:index]
        num = 0 if digitPart == '' else int(digitPart)

        if negative:
            num = min(negMax, num)
        else:
            num = min(posMax, num)

        return -num if negative else num

if __name__ == "__main__":
    sol = Solution()
    s = "42"
    s = "4193 with words"
    s = "-42"
    s = "-2147483647"
    s = "+"
    print(sol.myAtoi(s))
