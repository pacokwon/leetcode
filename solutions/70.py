# Climbing Stairs

class Solution:
    def climbStairs(self, n):
        a, b = 1, 2
        if n == 1:
            return a
        elif n == 2:
            return b

        for _ in range(3, n + 1):
            newB = a + b
            a = b
            b = newB

        return b

if __name__ == "__main__":
    sol = Solution()
    inp = 4
    print(sol.climbStairs(inp))
