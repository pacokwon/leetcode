# Find First Palindromic String in the Array

from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPal(word):
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False

                left += 1
                right -= 1
            return True

        for word in words:
            if isPal(word):
                return word

        return ""

if __name__ == "__main__":
    sol = Solution()
    words = ["abc","car","foo","bar","cool"]
    print( sol.firstPalindrome(words) )
