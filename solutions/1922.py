# Count Good Numbers

class Solution:
    def pow20(self, n):
        if n == 0:
            return 1

        modulo = 1000000007
        half = self.pow20(n // 2)
        if n % 2 == 0:
            return (half * half) % modulo
        else:
            return (half * half * 20) % modulo

    def countGoodNumbers(self, n):
        modulo = 1000000007
        if n % 2 == 0:
            return self.pow20(n // 2) % modulo
        else:
            return (self.pow20(n // 2) * 5) % modulo


if __name__ == "__main__":
    sol = Solution()
    inp = 50
    print(sol.countGoodNumbers(inp))
