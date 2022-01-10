# Length of Last Word

class Solution:
    def find(self, s, start, pred):
        index = start
        while index >= 0 and not pred(s[index]):
            index -= 1
        return index if pred(s[index]) else -1

    def lengthOfLastWord(self, s):
        length = len(s)
        firstChar = self.find(s, length - 1, lambda x: x != ' ')
        whitespace = self.find(s, firstChar, lambda x: x == ' ')
        return firstChar - whitespace

if __name__ == "__main__":
    sol = Solution()
    inp = "   fly me   to   the moon  "
    print(sol.lengthOfLastWord(inp))
