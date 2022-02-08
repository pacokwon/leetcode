# Add Digits

class Solution:
    def helper(self, num: int) -> int:
        added = 0
        while num != 0:
            added += num % 10
            num //= 10

        return added

    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = self.helper(num)
        return num

if __name__ == "__main__":
    sol = Solution()
    num = 38
    print(sol.addDigits(num))
