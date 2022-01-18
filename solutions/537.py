# Complex Number Multiplication
class Solution:
    def parseComplexNumber(self, num):
        [fst, snd] = num.split('+')
        return (int(fst), int(snd[:-1]))

    def complexNumberMultiply(self, num1, num2):
        [real1, imag1] = self.parseComplexNumber(num1)
        [real2, imag2] = self.parseComplexNumber(num2)
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        return f"{real}+{imag}i"

if __name__ == "__main__":
    sol = Solution()
    num1 = "1+-1i"
    num2 = "1+-1i"
    print(sol.complexNumberMultiply(num1, num2))
