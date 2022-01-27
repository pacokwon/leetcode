# Letter Case Permutation

class Solution:
    def letterCasePermutation(self, s):
        # list version
        ls = list(s)
        length = len(ls)

        def helper(choices, count, ans):
            if count == length:
                ans.append(''.join(choices))
                return

            c = choices[count]
            if '0' <= c <= '9':
                helper(choices, count + 1, ans)
            else:
                choices[count] = c.lower()
                helper(choices, count + 1, ans)

                choices[count] = c.upper()
                helper(choices, count + 1, ans)

        ans = []
        helper(ls, 0, ans)
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "3z4"
    print(sol.letterCasePermutation(s))
