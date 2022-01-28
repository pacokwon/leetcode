# Backspace String Compare

class Solution:
    def backspaceCompare(self, s, t):
        reals, realt = [], []
        for c in s:
            if c == '#':
                if reals:
                    reals.pop()
            else:
                reals.append(c)

        for c in t:
            if c == '#':
                if realt:
                    realt.pop()
            else:
                realt.append(c)

        return ''.join(reals) == ''.join(realt)

if __name__ == "__main__":
    sol = Solution()
    s = "ab#c"
    t = "ad#c"

    s = "ab##"
    t = "c#d#"

    s = "a#b"
    t = "c"

    s = "bxj##tw"
    t = "bxo#j##tw"

    s = "a##c"
    t = "#a#c"
    print( sol.backspaceCompare(s, t) )
