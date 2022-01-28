# Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        letters = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        length = len(digits)
        path = [None] * length

        if length == 0:
            return []

        def helper(index, path, ans):
            if index == length:
                ans.append(''.join(path))
                return

            digit = int(digits[index])
            for l in letters[digit]:
                path[index] = l
                helper(index + 1, path, ans)

        ans = []
        helper(0, path, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))
