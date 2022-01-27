# Reverse Words in a String III

class Solution:
    def reverseWords(self, s):
        return ' '.join(word[::-1] for word in s.split())

if __name__ == "__main__":
    sol = Solution()
    s = "God Ding"
    print(sol.reverseWords(s))
