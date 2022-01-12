# Integer to Roman

class Solution:
    formulas = [ "", "1", "11", "111", "15", "5", "51", "511", "5111", "1A" ]
    table = [{ "1": "I", "5": "V", "A": "X" }, { "1": "X", "5": "L", "A": "C" }, { "1": "C", "5": "D", "A": "M" }, { "1": "M" }]

    def convert(self, digit, exponent):
        formula = Solution.formulas[digit]
        table = Solution.table[exponent]
        return ''.join([table[d] for d in formula])

    def intToRoman(self, num):
        num = str(num)
        length = len(num)

        romanDigits = []
        for index, digit in enumerate(num):
            # the exponent with base of 10
            exponent = length - 1 - index
            romanDigits.append(self.convert(int(digit), exponent))

        return ''.join(romanDigits)

if __name__ == "__main__":
    sol = Solution()
    inp = 1904
    print(sol.intToRoman(inp))
