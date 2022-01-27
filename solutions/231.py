# Power of Two

class Solution:
    def isPowerOfTwo(self, n):
        product = 1
        while product < n:
            product *= 2

        return product == n

if __name__ == "__main__":
    sol = Solution()
