# Adding Spaces to a String

class Solution:
    def addSpaces(self, s, spaces):
        ans = [None] * (len(spaces) + 1)
        start = 0
        for index, sp in enumerate(spaces):
            if index == 0:
                end = start + sp
            else:
                end = start + sp - spaces[index - 1]
            ans[index] = s[start:end]
            start = end
        ans[len(spaces)] = s[start:]

        return " ".join(ans)

if __name__ == "__main__":
    sol = Solution()
    s = "LeetcodeHelpsMeLearn"
    spaces = [8,13,15]
    s = "icodeinpython"
    spaces = [1,5,7,9]
    s = "spacing"
    spaces = [0,1,2,3,4,5,6]
    print(sol.addSpaces(s, spaces))
