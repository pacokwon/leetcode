# Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))
