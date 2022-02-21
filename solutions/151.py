# Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))

# if __name__ == "__main__":
#     sol = Solution()
#     s = "the sky is blue"
#     s = "  hello world  "
#     s = " a good     example "
#     print(sol.reverseWords(s))
