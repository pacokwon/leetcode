class Solution:
    def plusOne(self, digits):
        sum = 0
        for d in digits:
            sum = 10 * sum + d

        return [int(c) for c in str(sum + 1)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([9, 9, 9]))
