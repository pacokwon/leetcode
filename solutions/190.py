# Reverse Bits


"""
4 bits
1111 -> 15
1111 -> 15

1011 -> 11
1101 -> 13

1001 -> 9
1001 -> 9

0011 -> 3
1100 -> 12

1010 -> 10
0101 -> 5
"""

class Solution:
    def reverseBits(self, n):
        n = ((n & 0xFFFF0000) >> 16) | ((n & 0x0000FFFF) << 16)
        n = ((n & 0xFF00FF00) >> 8)  | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4)  | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2)  | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1)  | ((n & 0x55555555) << 1)

        return n

if __name__ == "__main__":
    sol = Solution()
    inp = 0b11111111111111111111111111111101
    inp = 0b00000010100101000001111010011100
    print(sol.reverseBits(inp))
