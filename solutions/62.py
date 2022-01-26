# Unique Paths

class Solution:
    def uniquePaths(self, m, n):
        ans = 1
        added = m + n - 2
        smaller = min(m, n) - 1
        for i in range(1, smaller + 1):
            ans = ans * (added - i + 1) // i

        return ans

if __name__ == '__main__':
    sol = Solution()
    m = 3
    n = 7
    print(sol.uniquePaths(m, n))
