# Check if All A's Appears Before All B's

class Solution:
    def checkString(self, s: str) -> bool:
        current = 'a'
        for c in s:
            if current == 'a' and c == 'b':
                current = 'b'
            if current == 'b' and c == 'a':
                return False

        return True

