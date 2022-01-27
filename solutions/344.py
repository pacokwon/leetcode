# Reverse String

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        mid = length // 2
        for i in range(mid):
            s[i], s[length - 1 - i] = s[length - 1 - i], s[i]

if __name__ == "__main__":
    sol = Solution()
    s = ["h","e","l","l","o"]
    s = ["H","a","n","n","a","h"]
    sol.reverseString(s)
    print(s)
