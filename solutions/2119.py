# A Number After a Double Reversal

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        def rev(n):
            return int(str(n)[::-1])
        return num == rev(rev(num))

if __name__ == "__main__":
    sol = Solution()
    num = 0
    # num = 1800
    # num = 625
    print(sol.isSameAfterReversals(num))
