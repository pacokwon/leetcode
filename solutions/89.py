# Gray Code

class Solution:
    def grayCode(self, n):
        if n == 1:
            return [0, 1]

        shorterCodes = self.grayCode(n - 1)
        length = 2 ** n
        codes = [0] * length
        msb = 2 ** (n - 1)

        for index, sc in enumerate(shorterCodes):
            codes[index] = sc
            codes[length - 1 - index] = sc | msb

        return codes

if __name__ == "__main__":
    sol = Solution()
    inp = 3
    print(sol.grayCode(inp))
