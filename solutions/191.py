# Number of 1 Bits

class Solution:
    def hammingWeight(self, n):
        return 0 if n == 0 else 1 + self.hammingWeight(n & (n - 1))

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(0b00000000000000000000000000001011))
