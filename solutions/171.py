# Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        offset = ord('A') - 1
        for c in columnTitle:
            ans = ans * 26 + (ord(c) - offset)

        return ans
